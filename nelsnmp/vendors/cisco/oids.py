from nelsnmp.oids import GeneralOids


class CiscoOids(GeneralOids):
    """Statically define Cisco OIDs and inherit general oids

    """

    def __init__(self):

        super(CiscoOids, self).__init__()
        # From CISCO-CDP-MIB
        self.cdpInterfaceEntry = "1.3.6.1.4.1.9.9.23.1.1.1.1"
        self.cdpInterfaceEnable = "1.3.6.1.4.1.9.9.23.1.1.1.1.2"
        self.cdpCacheEntry = "1.3.6.1.4.1.9.9.23.1.2.1.1"
        self.cdpCacheDeviceId = "1.3.6.1.4.1.9.9.23.1.2.1.1.6"
        self.cdpCacheDevicePort = "1.3.6.1.4.1.9.9.23.1.2.1.1.7"
        self.cdpCacheAddressType = "1.3.6.1.4.1.9.9.23.1.2.1.1.3"
        self.cdpCacheAddress = "1.3.6.1.4.1.9.9.23.1.2.1.1.4"
        self.cdpGlobalRun = "1.3.6.1.4.1.9.9.23.1.3.1"
        self.cdpGlobalMessageInterval = "1.3.6.1.4.1.9.9.23.1.3.2"
        self.cdpGlobalHoldTime = "1.3.6.1.4.1.9.9.23.1.3.3"

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

        self.vlanTrunkPortEncapsulationType = "1.3.6.1.4.1.9.9.46.1.6.1.1.3"
        self.vlanTrunkPortVlansEnabled = "1.3.6.1.4.1.9.9.46.1.6.1.1.4"
        self.vlanTrunkPortNativeVlan = "1.3.6.1.4.1.9.9.46.1.6.1.1.5"
        self.vlanTrunkPortDynamicState = "1.3.6.1.4.1.9.9.46.1.6.1.1.13"
        self.vlanTrunkPortDynamicStatus = "1.3.6.1.4.1.9.9.46.1.6.1.1.14"
        self.vlanTrunkPortEncapsulationOperType = "1.3.6.1.4.1.9.9.46.1.6.1.1.16"
        self.vlanTrunkPortVlansEnabled2k = "1.3.6.1.4.1.9.9.46.1.6.1.1.17"
        self.vlanTrunkPortVlansEnabled3k = "1.3.6.1.4.1.9.9.46.1.6.1.1.18"
        self.vlanTrunkPortVlansEnabled4k = "1.3.6.1.4.1.9.9.46.1.6.1.1.19"
        self.vlanTrunkPortSetSerialNo = "1.3.6.1.4.1.9.9.46.1.6.2"


        # From CISCO-VLAN-MEMBERSHIP-MIB
        self.vmVlan = "1.3.6.1.4.1.9.9.68.1.2.2.1.2"

        # From CISCO-STP-EXTENSIONS-MIB
        self.stpxSpanningTreeType = "1.3.6.1.4.1.9.9.82.1.6.1"

        # From CISCO-CONFIG-COPY-MIB
        self.ccCopyProtocol = "1.3.6.1.4.1.9.9.96.1.1.1.1.2"
        self.ccCopySourceFileType = "1.3.6.1.4.1.9.9.96.1.1.1.1.3"
        self.ccCopyDestFileType = "1.3.6.1.4.1.9.9.96.1.1.1.1.4"
        self.ccCopyServerAddress = "1.3.6.1.4.1.9.9.96.1.1.1.1.5"
        self.ccCopyFileName = "1.3.6.1.4.1.9.9.96.1.1.1.1.6"
        self.ccCopyUserName = "1.3.6.1.4.1.9.9.96.1.1.1.1.7"
        self.ccCopyUserPassword = "1.3.6.1.4.1.9.9.96.1.1.1.1.8"
        self.ccCopyNotificationOnCompletion = "1.3.6.1.4.1.9.9.96.1.1.1.1.9"
        self.ccCopyState = "1.3.6.1.4.1.9.9.96.1.1.1.1.10"
        self.ccCopyTimeStarted = "1.3.6.1.4.1.9.9.96.1.1.1.1.11"
        self.ccCopyTimeCompleted = "1.3.6.1.4.1.9.9.96.1.1.1.1.12"
        self.ccCopyFailCause = "1.3.6.1.4.1.9.9.96.1.1.1.1.13"
        self.ccCopyEntryRowStatus = "1.3.6.1.4.1.9.9.96.1.1.1.1.14"
        self.ccCopyServerAddressType = "1.3.6.1.4.1.9.9.96.1.1.1.1.15"
        self.ccCopyServerAddressRev1 = "1.3.6.1.4.1.9.9.96.1.1.1.1.16"

        # From CISCO-FIREWALL-MIB
        self.cfwConnectionStatValue = "1.3.6.1.4.1.9.9.147.1.2.2.2.1.5"

        # From CISCO-L2L3-INTERFACE-CONFIG-MIB
        self.cL2L3IfModeAdmin = "1.3.6.1.4.1.9.9.151.1.1.1.1.1"

        # From CISCO-PAE-MIB
        self.cpaePortMode = "1.3.6.1.4.1.9.9.220.1.1.1.2"
        self.cpaeGuestVlanNumber = "1.3.6.1.4.1.9.9.220.1.1.1.3"
        self.cpaeShutdownTimeoutEnabled = "1.3.6.1.4.1.9.9.220.1.1.1.5"
        self.cpaePortAuthFailVlan = "1.3.6.1.4.1.9.9.220.1.1.1.6"
        self.cpaePortOperVlan = "1.3.6.1.4.1.9.9.220.1.1.1.7"
        self.cpaePortOperVlanType = "1.3.6.1.4.1.9.9.220.1.1.1.8"
        self.cpaeAuthFailVlanMaxAttempts = "1.3.6.1.4.1.9.9.220.1.1.1.9"
        self.cpaePortCapabilitiesEnabled = "1.3.6.1.4.1.9.9.220.1.1.1.10"
        self.cpaeMacAuthBypassPortEnabled = "1.3.6.1.4.1.9.9.220.1.8.6.1.1"


        # From CISCO-LAG-MIB
        self.clagAggDistributionProtocol = "1.3.6.1.4.1.9.9.225.1.1.1"
        self.clagAggDistributionAddressMode = "1.3.6.1.4.1.9.9.225.1.1.2"

        # From CISCO-PORT-SECURITY-MIB
        self.cpsIfPortSecurityEnable = "1.3.6.1.4.1.9.9.315.1.2.1.1.1"
        self.cpsIfPortSecurityStatus = "1.3.6.1.4.1.9.9.315.1.2.1.1.2"
        self.cpsIfMaxSecureMacAddr = "1.3.6.1.4.1.9.9.315.1.2.1.1.3"
        self.cpsIfCurrentSecureMacAddrCount = "1.3.6.1.4.1.9.9.315.1.2.1.1.4"
        self.cpsIfSecureMacAddrAgingTime = "1.3.6.1.4.1.9.9.315.1.2.1.1.5"
        self.cpsIfSecureMacAddrAgingType = "1.3.6.1.4.1.9.9.315.1.2.1.1.6"
        self.cpsIfStaticMacAddrAgingEnable = "1.3.6.1.4.1.9.9.315.1.2.1.1.7"
        self.cpsIfViolationAction = "1.3.6.1.4.1.9.9.315.1.2.1.1.8"
        self.cpsIfViolationCount = "1.3.6.1.4.1.9.9.315.1.2.1.1.9"
        self.cpsIfSecureLastMacAddress = "1.3.6.1.4.1.9.9.315.1.2.1.1.10"
        self.cpsIfUnicastFloodingEnable = "1.3.6.1.4.1.9.9.315.1.2.1.1.12"
        self.cpsIfShutdownTimeout = "1.3.6.1.4.1.9.9.315.1.2.1.1.13"
        self.cpsIfClearSecureMacAddresses = "1.3.6.1.4.1.9.9.315.1.2.1.1.14"
        self.cpsIfStickyEnable = "1.3.6.1.4.1.9.9.315.1.2.1.1.15"
        self.cpsIfInvalidSrcRateLimitEnable = "1.3.6.1.4.1.9.9.315.1.2.1.1.16"
        self.cpsIfInvalidSrcRateLimitValue = "1.3.6.1.4.1.9.9.315.1.2.1.1.17"
        self.cpsIfSecureLastMacAddrVlanId = "1.3.6.1.4.1.9.9.315.1.2.1.1.18"
