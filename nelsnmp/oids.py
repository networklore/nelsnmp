

class GeneralOids(object):
    """Statically define general oids
    """

    def __init__(self):

        # From SNMPv2-MIB
        self.sysDescr = "1.3.6.1.2.1.1.1"
        self.sysObjectId = "1.3.6.1.2.1.1.2"
        self.sysUpTime   = "1.3.6.1.2.1.1.3"
        self.sysContact  = "1.3.6.1.2.1.1.4"
        self.sysName     = "1.3.6.1.2.1.1.5"
        self.sysLocation = "1.3.6.1.2.1.1.6"

        # From IF-MIB
        self.ifTable       = "1.3.6.1.2.1.2.2"
        self.ifEntry       = "1.3.6.1.2.1.2.2.1"
        self.ifIndex       = "1.3.6.1.2.1.2.2.1.1"
        self.ifDescr       = "1.3.6.1.2.1.2.2.1.2"
        self.ifMtu         = "1.3.6.1.2.1.2.2.1.4"
        self.ifSpeed       = "1.3.6.1.2.1.2.2.1.5"
        self.ifPhysAddress = "1.3.6.1.2.1.2.2.1.6"
        self.ifAdminStatus = "1.3.6.1.2.1.2.2.1.7"
        self.ifOperStatus  = "1.3.6.1.2.1.2.2.1.8"
        self.ifAlias       = "1.3.6.1.2.1.31.1.1.1.18"

        # From IP-MIB
        self.ipAdEntAddr    = "1.3.6.1.2.1.4.20.1.1"
        self.ipAdEntIfIndex = "1.3.6.1.2.1.4.20.1.2"
        self.ipAdEntNetMask = "1.3.6.1.2.1.4.20.1.3"

        # From HOST-RESOURCES-MIB
        self.hrStorageIndex = "1.3.6.1.2.1.25.2.3.1.1"
        self.hrStorageType = "1.3.6.1.2.1.25.2.3.1.2"
        self.hrStorageDescr = "1.3.6.1.2.1.25.2.3.1.3"
        self.hrStorageAllocationUnits = "1.3.6.1.2.1.25.2.3.1.4"
        self.hrStorageSize = "1.3.6.1.2.1.25.2.3.1.5"
        self.hrStorageUsed = "1.3.6.1.2.1.25.2.3.1.6"
        self.hrStorageAllocationFailures = "1.3.6.1.2.1.25.2.3.1.7"
                       
        # From ENTITY-MIB
        self.entPhysicalDescr = "1.3.6.1.2.1.47.1.1.1.1.2"
        self.entPhysicalName = "1.3.6.1.2.1.47.1.1.1.1.7"
        self.entPhysicalHardwareRev = "1.3.6.1.2.1.47.1.1.1.1.8"
        self.entPhysicalFirmwareRev = "1.3.6.1.2.1.47.1.1.1.1.9"
        self.entPhysicalSoftwareRev = "1.3.6.1.2.1.47.1.1.1.1.10"
        self.entPhysicalSerialNum = "1.3.6.1.2.1.47.1.1.1.1.11"
        self.entPhysicalMfgName = "1.3.6.1.2.1.47.1.1.1.1.12"
        self.entPhysicalModelName = "1.3.6.1.2.1.47.1.1.1.1.13"



