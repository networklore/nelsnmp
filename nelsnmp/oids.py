

class DefineOid(object):
    """Statically define oids instead of using MIB

    Class Arguments
    get: While using snmp get a period needs to be added before the numeric oid
    set: When setting snmp values the oid needs to be presented as a tuple
    value: When looking at the return values from a query use the oid as is
    """

    def __init__(self, snmptype):
        if snmptype != "get" and snmptype != "set" and snmptype != "value":
            # return "ERROR"
            sys.exit()

        self.snmp_type = snmptype

        # From SNMPv2-MIB
        self.sysDescr = self.fo(
            "1.3.6.1.2.1.1.1")
        self.sysObjectId = self.fo("1.3.6.1.2.1.1.2")
        self.sysUpTime   = self.fo("1.3.6.1.2.1.1.3")
        self.sysContact  = self.fo("1.3.6.1.2.1.1.4")
        self.sysName     = self.fo("1.3.6.1.2.1.1.5")
        self.sysLocation = self.fo("1.3.6.1.2.1.1.6")

        # From IF-MIB
        self.ifIndex       = self.fo("1.3.6.1.2.1.2.2.1.1")
        self.ifDescr       = self.fo("1.3.6.1.2.1.2.2.1.2")
        self.ifMtu         = self.fo("1.3.6.1.2.1.2.2.1.4")
        self.ifSpeed       = self.fo("1.3.6.1.2.1.2.2.1.5")
        self.ifPhysAddress = self.fo("1.3.6.1.2.1.2.2.1.6")
        self.ifAdminStatus = self.fo("1.3.6.1.2.1.2.2.1.7")
        self.ifOperStatus  = self.fo("1.3.6.1.2.1.2.2.1.8")
        self.ifAlias       = self.fo("1.3.6.1.2.1.31.1.1.1.18")

        # From IP-MIB
        self.ipAdEntAddr    = self.fo("1.3.6.1.2.1.4.20.1.1")
        self.ipAdEntIfIndex = self.fo("1.3.6.1.2.1.4.20.1.2")
        self.ipAdEntNetMask = self.fo("1.3.6.1.2.1.4.20.1.3")

        # From CISCO-FIREWALL-MIB
        self.cfwConnectionStatValue = self.fo(
            "1.3.6.1.4.1.9.9.147.1.2.2.2.1.5")


    # format_oid
    def fo(self, oid):

        if self.snmp_type == 'get':
            return "." + oid
        if self.snmp_type == 'value':
            return oid
        if self.snmp_type == 'set':
            oidlist = list(oid.split("."))
            return map(int, oidlist)
