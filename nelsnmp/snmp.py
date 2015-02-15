from pysnmp.entity.rfc3413.oneliner import cmdgen

SNMP_VERSIONS = ('2c', '3')

class SnmpHandler(object):
    

    def __init__(self, **kwargs):

        self.port = 161
        self.version = False
        self.community = False
        self.host = False


        for key in kwargs:
            print key, kwargs[key]
            if key == 'version' and kwargs[key] in SNMP_VERSIONS:   
                self.version = kwargs[key]
            if key == 'community':
                self.community = kwargs[key]
            if key == 'host':
                self.host = kwargs[key]

        if self.version == False or self.host == False:
            print "You have to set version and host"
        if self.version == "2c":
            self.snmp_auth = cmdgen.CommunityData(self.community)

    def snmp_get(self, *oidlist):

        snmp_query = []
        for oid in oidlist:
            snmp_query.append(cmdgen.MibVariable(oid,), )

        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
            self.snmp_auth,
            cmdgen.UdpTransportTarget((self.host, self.port)),
            *snmp_query
        )

        if errorIndication:
            nelmon.common.exit_with_error(errorIndication)

        if errorStatus:
            nelmon.common.exit_with_error(errorStatus)

        return varBinds


    def snmp_getnext(self, *oidlist):

        snmp_query = []
        for oid in oidlist:
            snmp_query.append(cmdgen.MibVariable(oid,), )

        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.nextCmd(
            self.snmp_auth,
            cmdgen.UdpTransportTarget((self.host, self.port)),
            *snmp_query
        )

        if errorIndication:
            nelmon.common.exit_with_error(errorIndication)

        if errorStatus:
            nelmon.common.exit_with_error(errorStatus)

        return varBinds

