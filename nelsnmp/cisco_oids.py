from nelsnmp.oids import GeneralOids


class CiscoOids(GeneralOids):
    """Statically define oids instead of using MIB

    """

    def __init__(self):

        super(CiscoOids, self).__init__()

        # From CISCO-VTP-MIB
        self.vtpVlanIndex = "1.3.6.1.4.1.9.9.46.1.3.1.1.1"
        self.vtpVlanState = "1.3.6.1.4.1.9.9.46.1.3.1.1.2"
        self.vtpVlanName = "1.3.6.1.4.1.9.9.46.1.3.1.1.4"       
        self.vtpVlanEditOperation = "1.3.6.1.4.1.9.9.46.1.4.1.1.1"
        self.vtpVlanEditBufferOwner = "1.3.6.1.4.1.9.9.46.1.4.1.1.3"
        self.vtpVlanEditTable = "1.3.6.1.4.1.9.9.46.1.4.2"
        self.vtpVlanApplyStatus = "1.3.6.1.4.1.9.9.46.1.4.1.1.2"
        self.vtpVlanEditType = "1.3.6.1.4.1.9.9.46.1.4.2.1.3"
        self.vtpVlanEditName = "1.3.6.1.4.1.9.9.46.1.4.2.1.4"
        self.vtpVlanEditDot10Said = "1.3.6.1.4.1.9.9.46.1.4.2.1.6"
        self.vtpVlanEditRowStatus = "1.3.6.1.4.1.9.9.46.1.4.2.1.11"

        # From CISCO-CONFIG-COPY-MIB
        self.ccCopySourceFileType = "1.3.6.1.4.1.9.9.96.1.1.1.1.3"
        self.ccCopyDestFileType = "1.3.6.1.4.1.9.9.96.1.1.1.1.4"
        self.ccCopyState = "1.3.6.1.4.1.9.9.96.1.1.1.1.10"
        self.ccCopyEntryRowStatus = "1.3.6.1.4.1.9.9.96.1.1.1.1.14"

        # From CISCO-FIREWALL-MIB
        self.cfwConnectionStatValue = "1.3.6.1.4.1.9.9.147.1.2.2.2.1.5"

