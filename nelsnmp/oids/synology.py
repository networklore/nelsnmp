from nelsnmp.oids import GeneralOids


class SynologyOids(GeneralOids):
    """Statically define Synology OIDs and inherit general oids

    """

    def __init__(self):

        super(SynologyOids, self).__init__()
        self.synology = "1.3.6.1.4.1.6574"

        # From SYNOLOGY-SYSTEM-MIB
        self.synoSystem = "1.3.6.1.4.1.6574.1"
        self.systemStatus = "1.3.6.1.4.1.6574.1.1"
        self.temperature = "1.3.6.1.4.1.6574.1.2"
        self.powerStatus = "1.3.6.1.4.1.6574.1.3"
        self.fan = "1.3.6.1.4.1.6574.1.4"
        self.systemFanStatus = "1.3.6.1.4.1.6574.1.4.1"
        self.cpuFanStatus = "1.3.6.1.4.1.6574.1.4.2"
        self.dsmInfo = "1.3.6.1.4.1.6574.1.5"
        self.modelName = "1.3.6.1.4.1.6574.1.5.1"
        self.serialNumber = "1.3.6.1.4.1.6574.1.5.2"
        self.version = "1.3.6.1.4.1.6574.1.5.3"
        self.upgradeAvailable = "1.3.6.1.4.1.6574.1.5.4"

        # From SYNOLOGY-DISK-MIB
        self.synoDisk = "1.3.6.1.4.1.6574.2"
        self.diskTable = "1.3.6.1.4.1.6574.2.1"
        self.diskEntry = "1.3.6.1.4.1.6574.2.1.1"
        self.diskIndex = "1.3.6.1.4.1.6574.2.1.1.1"
        self.diskID = "1.3.6.1.4.1.6574.2.1.1.2"
        self.diskModel = "1.3.6.1.4.1.6574.2.1.1.3"
        self.diskType = "1.3.6.1.4.1.6574.2.1.1.4"
        self.diskStatus = "1.3.6.1.4.1.6574.2.1.1.5"
        self.diskTemperature = "1.3.6.1.4.1.6574.2.1.1.6"

        # From SYNOLOGY-RAID-MIB
        self.synoRaid = "1.3.6.1.4.1.6574.3"
        self.raidTable = "1.3.6.1.4.1.6574.3.1"
        self.raidEntry = "1.3.6.1.4.1.6574.3.1.1"
        self.raidIndex = "1.3.6.1.4.1.6574.3.1.1.1"
        self.raidName = "1.3.6.1.4.1.6574.3.1.1.2"
        self.raidStatus = "1.3.6.1.4.1.6574.3.1.1.3"
