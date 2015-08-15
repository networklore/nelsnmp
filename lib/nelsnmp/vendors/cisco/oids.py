from nelsnmp.oids import GeneralOids


class CiscoOids(GeneralOids):
    """Statically define Cisco OIDs and inherit general oids

    """

    def __init__(self):

        super(CiscoOids, self).__init__()
        # From CISCO-ENVMON-MIB
        self.ciscoEnvMonMIB = '1.3.6.1.4.1.9.9.13'
        self.ciscoEnvMonObjects = '1.3.6.1.4.1.9.9.13.1'
        self.ciscoEnvMonPresent = '1.3.6.1.4.1.9.9.13.1.1'
        self.ciscoEnvMonVoltageStatusTable = '1.3.6.1.4.1.9.9.13.1.2'
        self.ciscoEnvMonVoltageStatusEntry = '1.3.6.1.4.1.9.9.13.1.2.1'
        self.ciscoEnvMonVoltageStatusIndex = '1.3.6.1.4.1.9.9.13.1.2.1.1'
        self.ciscoEnvMonVoltageStatusDescr = '1.3.6.1.4.1.9.9.13.1.2.1.2'
        self.ciscoEnvMonVoltageStatusValue = '1.3.6.1.4.1.9.9.13.1.2.1.3'
        self.ciscoEnvMonVoltageThresholdLow = '1.3.6.1.4.1.9.9.13.1.2.1.4'
        self.ciscoEnvMonVoltageThresholdHigh = '1.3.6.1.4.1.9.9.13.1.2.1.5'
        self.ciscoEnvMonVoltageLastShutdown = '1.3.6.1.4.1.9.9.13.1.2.1.6'
        self.ciscoEnvMonVoltageState = '1.3.6.1.4.1.9.9.13.1.2.1.7'
        self.ciscoEnvMonTemperatureStatusTable = '1.3.6.1.4.1.9.9.13.1.3'
        self.ciscoEnvMonTemperatureStatusEntry = '1.3.6.1.4.1.9.9.13.1.3.1'
        self.ciscoEnvMonTemperatureStatusIndex = '1.3.6.1.4.1.9.9.13.1.3.1.1'
        self.ciscoEnvMonTemperatureStatusDescr = '1.3.6.1.4.1.9.9.13.1.3.1.2'
        self.ciscoEnvMonTemperatureStatusValue = '1.3.6.1.4.1.9.9.13.1.3.1.3'
        self.ciscoEnvMonTemperatureThreshold = '1.3.6.1.4.1.9.9.13.1.3.1.4'
        self.ciscoEnvMonTemperatureLastShutdown = '1.3.6.1.4.1.9.9.13.1.3.1.5'
        self.ciscoEnvMonTemperatureState = '1.3.6.1.4.1.9.9.13.1.3.1.6'
        self.ciscoEnvMonFanStatusTable = '1.3.6.1.4.1.9.9.13.1.4'
        self.ciscoEnvMonFanStatusEntry = '1.3.6.1.4.1.9.9.13.1.4.1'
        self.ciscoEnvMonFanStatusIndex = '1.3.6.1.4.1.9.9.13.1.4.1.1'
        self.ciscoEnvMonFanStatusDescr = '1.3.6.1.4.1.9.9.13.1.4.1.2'
        self.ciscoEnvMonFanState = '1.3.6.1.4.1.9.9.13.1.4.1.3'
        self.ciscoEnvMonSupplyStatusTable = '1.3.6.1.4.1.9.9.13.1.5'
        self.ciscoEnvMonSupplyStatusEntry = '1.3.6.1.4.1.9.9.13.1.5.1'
        self.ciscoEnvMonSupplyStatusIndex = '1.3.6.1.4.1.9.9.13.1.5.1.1'
        self.ciscoEnvMonSupplyStatusDescr = '1.3.6.1.4.1.9.9.13.1.5.1.2'
        self.ciscoEnvMonSupplyState = '1.3.6.1.4.1.9.9.13.1.5.1.3'
        self.ciscoEnvMonSupplySource = '1.3.6.1.4.1.9.9.13.1.5.1.4'
        self.ciscoEnvMonAlarmContacts = '1.3.6.1.4.1.9.9.13.1.6'

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

        # From CISCO-RTTMON-MIB
        self.ciscoRttMonMIB = '1.3.6.1.4.1.9.9.42'
        self.rttMonCtrlAdminEntry = '1.3.6.1.4.1.9.9.42.1.2.1.1'
        self.rttMonCtrlAdminIndex = '1.3.6.1.4.1.9.9.42.1.2.1.1.1'
        self.rttMonCtrlAdminOwner = '1.3.6.1.4.1.9.9.42.1.2.1.1.2'
        self.rttMonCtrlAdminTag = '1.3.6.1.4.1.9.9.42.1.2.1.1.3'
        self.rttMonCtrlAdminRttType = '1.3.6.1.4.1.9.9.42.1.2.1.1.4'
        self.rttMonCtrlAdminThreshold = '1.3.6.1.4.1.9.9.42.1.2.1.1.5'
        self.rttMonCtrlAdminFrequency = '1.3.6.1.4.1.9.9.42.1.2.1.1.6'
        self.rttMonCtrlAdminTimeout = '1.3.6.1.4.1.9.9.42.1.2.1.1.7'
        self.rttMonCtrlAdminVerifyData = '1.3.6.1.4.1.9.9.42.1.2.1.1.8'
        self.rttMonCtrlAdminStatus = '1.3.6.1.4.1.9.9.42.1.2.1.1.9'
        self.rttMonCtrlAdminNvgen = '1.3.6.1.4.1.9.9.42.1.2.1.1.10'
        self.rttMonCtrlAdminGroupName = '1.3.6.1.4.1.9.9.42.1.2.1.1.11'
        self.rttMonLatestRttOperEntry = '1.3.6.1.4.1.9.9.42.1.2.10.1'
        self.rttMonLatestRttOperCompletionTime = '1.3.6.1.4.1.9.9.42.1.2.10.1.1'
        self.rttMonLatestRttOperSense = '1.3.6.1.4.1.9.9.42.1.2.10.1.2'
        self.rttMonLatestRttOperApplSpecificSense = '1.3.6.1.4.1.9.9.42.1.2.10.1.3'
        self.rttMonLatestRttOperSenseDescription = '1.3.6.1.4.1.9.9.42.1.2.10.1.4'
        self.rttMonLatestRttOperTime = '1.3.6.1.4.1.9.9.42.1.2.10.1.5'
        self.rttMonLatestRttOperAddress = '1.3.6.1.4.1.9.9.42.1.2.10.1.6'

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

        # From CISCO-ENTITY-SENSOR-MIB
        self.entitySensorMIBObjects = '1.3.6.1.4.1.9.9.91.1'
        self.entSensorValues = '1.3.6.1.4.1.9.9.91.1.1'
        self.entSensorValueTable = '1.3.6.1.4.1.9.9.91.1.1.1'
        self.entSensorValueEntry = '1.3.6.1.4.1.9.9.91.1.1.1.1'
        self.entSensorType = '1.3.6.1.4.1.9.9.91.1.1.1.1.1'
        self.entSensorScale = '1.3.6.1.4.1.9.9.91.1.1.1.1.2'
        self.entSensorPrecision = '1.3.6.1.4.1.9.9.91.1.1.1.1.3'
        self.entSensorValue = '1.3.6.1.4.1.9.9.91.1.1.1.1.4'
        self.entSensorStatus = '1.3.6.1.4.1.9.9.91.1.1.1.1.5'
        self.entSensorValueTimeStamp = '1.3.6.1.4.1.9.9.91.1.1.1.1.6'
        self.entSensorValueUpdateRate = '1.3.6.1.4.1.9.9.91.1.1.1.1.7'
        self.entSensorMeasuredEntity = '1.3.6.1.4.1.9.9.91.1.1.1.1.8'

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
