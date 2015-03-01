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


SNMP_VERSIONS = ('2c', '3')




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
    if isinstance(value, OctetString):
        try:
            return value.asOctets().decode(value.encoding)
        except UnicodeDecodeError:
            return value.asOctets()
    if isinstance(value, TimeTicks):
        return timedelta(seconds=int(value.prettyPrint()) / 100.0)
    return value    

class SnmpHandler(object):
    

    def __init__(self, **kwargs):

        self.port = 161
        self.version = False
        self.community = False
        self.host = False
        self.errors = "raise"


        for key in kwargs:
            if key == 'version' and kwargs[key] in SNMP_VERSIONS:   
                self.version = kwargs[key]
            if key == 'community':
                self.community = kwargs[key]
            if key == 'host':
                self.host = kwargs[key]

        if self.version not in SNMP_VERSIONS:
            raise ArgumentError('No valid SNMP version defined')

        if self.version == False or self.host == False:
            print "You have to set version and host"
        if self.version == "2c":
            self.snmp_auth = cmdgen.CommunityData(self.community)

    def get(self, *oidlist):

        snmp_query = []
        for oid in oidlist:
            #snmp_query.append(cmdgen.MibVariable(oid,), )
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
        #return varBinds


    def getnext(self, *oidlist):

        snmp_query = []
        for oid in oidlist:
            #snmp_query.append(cmdgen.MibVariable(oid,), )
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

        #return varTable
        return pretty_vartable

    def set(self, *snmp_sets):

        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varTable = cmdGen.setCmd(
            self.snmp_auth,
            cmdgen.UdpTransportTarget((self.host, self.port)),
            *snmp_sets
        )

        if errorIndication or errorStatus:
            # Fix error handling
            pass

