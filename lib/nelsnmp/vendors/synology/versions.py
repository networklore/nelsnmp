from nelsnmp.hostinfo.version import DeviceVersion
from nelsnmp.vendors.synology.oids import SynologyOids


class SynologyVersion(DeviceVersion):

    def _get_version(self):
        self.vendor = 'synology'
        o = SynologyOids()
        vartable = self._snmp.getnext(o.version)
        for varbinds in vartable:
            for oid, value in varbinds:
                if o.version in oid:
                    self.os = 'dsm'
                    version_string = value.split()
                    if version_string[0] == 'DSM' and len(version_string) > 1:
                        self.version = version_string[1]
