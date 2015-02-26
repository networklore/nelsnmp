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

        # From CISCO-VTP-MIB
        self.vtpVlanIndex = self.fo(
            "1.3.6.1.4.1.9.9.46.1.3.1.1.1")
        self.vtpVlanState = self.fo(
            "1.3.6.1.4.1.9.9.46.1.3.1.1.2")
        self.vtpVlanName = self.fo(
            "1.3.6.1.4.1.9.9.46.1.3.1.1.4")       
        self.vtpVlanEditOperation = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.1.1.1")
        self.vtpVlanEditBufferOwner = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.1.1.3")
        self.vtpVlanEditTable = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.2")
        self.vtpVlanApplyStatus = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.1.1.2")
        self.vtpVlanEditType = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.2.1.3")
        self.vtpVlanEditName = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.2.1.4")
        self.vtpVlanEditDot10Said = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.2.1.6")
        self.vtpVlanEditRowStatus = self.fo(
            "1.3.6.1.4.1.9.9.46.1.4.2.1.11")

        # From CISCO-CONFIG-COPY-MIB
        self.ccCopySourceFileType = self.fo(
            "1.3.6.1.4.1.9.9.96.1.1.1.1.3")
        self.ccCopyDestFileType = self.fo(
            "1.3.6.1.4.1.9.9.96.1.1.1.1.4")
        self.ccCopyState = self.fo(
            "1.3.6.1.4.1.9.9.96.1.1.1.1.10")
        self.ccCopyEntryRowStatus = self.fo(
            "1.3.6.1.4.1.9.9.96.1.1.1.1.14")

        # From CISCO-FIREWALL-MIB
        self.cfwConnectionStatValue = self.fo(
            "1.3.6.1.4.1.9.9.147.1.2.2.2.1.5")

