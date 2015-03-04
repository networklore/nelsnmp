

class GeneralOids(object):
    """Statically define oids instead of using MIB

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
                       
        # From ENTITY-MIB
        self.entPhysicalDescr = "1.3.6.1.2.1.47.1.1.1.1.2"
        self.entPhysicalSerialNum = "1.3.6.1.2.1.47.1.1.1.1.11"
        