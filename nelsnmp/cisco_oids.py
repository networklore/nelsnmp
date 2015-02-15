from nelsnmp.oids import GeneralOids


class CiscoOids(GeneralOids):
    """Statically define oids instead of using MIB

    Class Arguments
    get: While using snmp get a period needs to be added before the numeric oid
    set: When setting snmp values the oid needs to be presented as a tuple
    value: When looking at the return values from a query use the oid as is
    """

    def __init__(self, snmptype):

        super(CiscoOids, self).__init__(snmptype)

        # From CISCO-FIREWALL-MIB
        self.cfwConnectionStatValue = self.fo(
            "1.3.6.1.4.1.9.9.147.1.2.2.2.1.5")
