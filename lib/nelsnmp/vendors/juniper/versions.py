from nelsnmp.hostinfo.version import DeviceVersion
from nelsnmp.oids import GeneralOids


class JuniperVersion(DeviceVersion):

    def _get_version(self):
        o = GeneralOids()

        varbind = self._snmp.get(o.hrSWInstalledName + '.2')
        for oid, value in varbind:
            parts = value.split()
            if parts[0] == 'JUNOS':
                self.os = 'junos'
                self.version = parts[-1][1:-1]
