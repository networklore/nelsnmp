from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import (
    Counter32,
    Counter64,
    Gauge32,
    Integer,
    Integer32,
    IpAddress,
    OctetString,
    TimeTicks,
    Unsigned32,
)
from pyasn1.type.univ import ObjectIdentifier
from datetime import timedelta

VALID_VERSIONS = ('2c', '3')
VALID_V3_LEVELS = ('authNoPriv', 'authPriv')
VALID_INTEGRITY_ALGO = ('md5', 'sha')
VALID_PRIVACY_ALGO = ('des', '3des', 'aes', 'aes192', 'aes256')

TYPES = {
    'Counter32': Counter32,
    'Counter64': Counter64,
    'Gauge32': Gauge32,
    'Integer': Integer,
    'Integer32': Integer32,
    'IpAddress': IpAddress,
    'OctetString': OctetString,
    'TimeTicks': TimeTicks,
    'Unsigned32': Unsigned32,
}

INTEGRITY_ALGO = {
    'md5': cmdgen.usmHMACMD5AuthProtocol,
    'sha': cmdgen.usmHMACSHAAuthProtocol
}

PRIVACY_ALGO = {
    'aes': cmdgen.usmAesCfb128Protocol,
    'aes192': cmdgen.usmAesCfb192Protocol,
    'aes256': cmdgen.usmAesCfb256Protocol,
    'des': cmdgen.usmDESPrivProtocol,
    '3des': cmdgen.usm3DESEDEPrivProtocol
}

class ArgumentError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)    

class SnmpError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def is_ipv4_address(value):
    try:
        c1, c2, c3, c4 = value.split(".")
        assert 0 <= int(c1) <= 255
        assert 0 <= int(c2) <= 255
        assert 0 <= int(c3) <= 255
        assert 0 <= int(c4) <= 255
        return True
    except:
        return False

def return_pretty_val(value):
    if isinstance(value, Counter32):
        return int(value.prettyPrint())
    if isinstance(value, Counter64):
        return int(value.prettyPrint())
    if isinstance(value, Gauge32):
        return int(value.prettyPrint())
    if isinstance(value, Integer):
        return int(value.prettyPrint())
    if isinstance(value, Integer32):
        return int(value.prettyPrint())
    if isinstance(value, Unsigned32):
        return int(value.prettyPrint())
    if isinstance(value, IpAddress):
        return str(value.prettyPrint())
    if isinstance(value, ObjectIdentifier):
        return str(value.prettyPrint())
    if isinstance(value, OctetString):
        try:
            return value.asOctets().decode(value.encoding)
        except UnicodeDecodeError:
            return value.asOctets()
    if isinstance(value, TimeTicks):
        return timedelta(seconds=int(value.prettyPrint()) / 100.0)
    return value    

def return_snmp_data(value,value_type):
    if value_type is None:
        if isinstance(value, int):
            data = Integer(value)
        elif isinstance(value, float):
            data = Integer(value)
        elif isinstance(value, str):
            if is_ipv4_address(value):
                data = IpAddress(value)
            else:
                data = OctetString(value)
        else:
            raise TypeError(
                "Unable to autodetect type. Please pass one of "
                "these strings as the value_type keyword arg: "
                ", ".join(TYPES.keys())
            )
    else:
        if not value_type in TYPES:
            raise ValueError("'{}' is not one of the supported types: {}".format(
                value_type,
                ", ".join(TYPES.keys())
            ))

        data = TYPES[value_type](value)
    return data

class SnmpHandler(object):
    

    def __init__(self, **kwargs):

        self.port = 161
        self.version = False
        self.community = False
        self.host = False
        self.username = False
        self.level = False
        self.integrity = False
        self.privacy = False
        self.authkey = False
        self.privkey = False
        self.errors = "raise"


        for key in kwargs:
            if key == 'version':
                if kwargs[key] in VALID_VERSIONS:   
                    self.version = kwargs[key]
                else:
                    raise ArgumentError('No valid SNMP version defined')       
            if key == 'community':
                self.community = kwargs[key]
            if key == 'host':
                self.host = kwargs[key]
            if key == 'port':
                if 1 <= kwargs[key] <= 65535:
                    self.port = kwargs[key]
                else:
                    raise ArgumentError('Port must be between 1 and 65535')
            if key == 'username':
                self.username = kwargs[key]
            if key == 'level':
                if kwargs[key] in VALID_V3_LEVELS:
                    self.level = kwargs[key]
                else:
                    raise ArgumentError('Security level invalid')
            if key == 'integrity':
                if kwargs[key] in VALID_INTEGRITY_ALGO:
                    self.integrity = kwargs[key]
                else:
                    raise ArgumentError('Integrity algorithm not valid')
            if key == 'privacy':
                if kwargs[key] in VALID_PRIVACY_ALGO:
                    self.privacy = kwargs[key]
                else:
                    raise ArgumentError('Privacy algorithm not valid')
            if key == 'authkey':
                self.authkey = kwargs[key]
            if key == 'privkey':
                self.privkey = kwargs[key]
          

        if self.host == False:
            raise ArgumentError('Host not defined')

        if self.version == "2c":
            self.snmp_auth = cmdgen.CommunityData(self.community)

        if self.version == "3":
            if self.username == False:
                raise ArgumentError('No username specified')
            if self.level == False:
                raise ArgumentError('No security level specified')
            if self.integrity == False:
                raise ArgumentError('No integrity protocol specified')
            if self.authkey == False:
                raise ArgumentError('No authkey specified')

            if self.level == 'authNoPriv':
                self.snmp_auth = cmdgen.UsmUserData(self.username,
                    authKey=self.authkey,
                    authProtocol=INTEGRITY_ALGO[self.integrity])
            elif self.level == 'authPriv':
                if self.privacy == False:
                    raise ArgumentError('No privacy protocol specified')
                if self.privkey == False:
                    raise ArgumentError('No privacy key specified')
                self.snmp_auth = cmdgen.UsmUserData(self.username,
                    authKey=self.authkey,
                    authProtocol=INTEGRITY_ALGO[self.integrity],
                    privKey=self.privkey,
                    privProtocol=PRIVACY_ALGO[self.privacy])
            else:
                raise ArgumentError('Unknown error') 


    def get(self, *oidlist):

        snmp_query = []
        for oid in oidlist:
            snmp_query.append(oid,)

        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
            self.snmp_auth,
            cmdgen.UdpTransportTarget((self.host, self.port)),
            *snmp_query
        )

        if errorIndication or errorStatus:
            current_error = errorIndication._ErrorIndication__descr
            if self.errors == "raise":
                raise SnmpError(current_error)

        pretty_varbinds = []
        for oid, value in varBinds:
            pretty_varbinds.append([oid.prettyPrint(), return_pretty_val(value)])

        return pretty_varbinds

    def get_value(self, *oidlist):

        snmp_query = []
        for oid in oidlist:
            snmp_query.append(oid,)

        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
            self.snmp_auth,
            cmdgen.UdpTransportTarget((self.host, self.port)),
            *snmp_query
        )

        if errorIndication or errorStatus:
            current_error = errorIndication._ErrorIndication__descr
            if self.errors == "raise":
                raise SnmpError(current_error)

        values = []
        for oid, value in varBinds:
            values.append(return_pretty_val(value))

        if len(values) == 1:
            values = values[0]

        return values


    def getnext(self, *oidlist):

        snmp_query = []
        for oid in oidlist:
            snmp_query.append(oid,)

        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varTable = cmdGen.nextCmd(
            self.snmp_auth,
            cmdgen.UdpTransportTarget((self.host, self.port)),
            *snmp_query
        )

        if errorIndication or errorStatus:
            current_error = errorIndication._ErrorIndication__descr
            if self.errors == "raise":
                raise SnmpError(current_error)

        pretty_vartable = []
        
        for varbinds in varTable:
            pretty_varbinds = []
            for oid, value in varbinds:
                pretty_varbinds.append([oid.prettyPrint(), return_pretty_val(value)])
            pretty_vartable.append(pretty_varbinds)

        return pretty_vartable

    def set(self,oid=None,value=None,value_type=None,multi=None):

        if multi is None:
            data = return_snmp_data(value,value_type)
            snmp_sets = (oid,data),
        else:
            snmp_sets = []
            for snmp_set in multi:
                print snmp_set
                if len(snmp_set) == 2:
                    oid = snmp_set[0]
                    value = snmp_set[1]
                    value_type = None
                    data = return_snmp_data(value,value_type)
                elif len(snmp_set) == 3:
                    oid = snmp_set[0]
                    value = snmp_set[1]
                    value_type = snmp_set[2]
                    data = return_snmp_data(value,value_type)
                snmp_sets.append((oid,data),)

        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varTable = cmdGen.setCmd(
            self.snmp_auth,
            cmdgen.UdpTransportTarget((self.host, self.port)),
            *snmp_sets
        )

        if errorIndication or errorStatus:
            #current_error = errorIndication._ErrorIndication__descr
            if self.errors == "raise":
                raise SnmpError(errorIndication)

