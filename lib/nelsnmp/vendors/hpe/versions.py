from nelsnmp.hostinfo.version import DeviceVersion


class HpeVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'ProCurve' in line:
                self.os = 'procurve'
                parts = line.split()
                if len(parts) > 5:
                    if parts[4] == 'revision':
                        self.version = parts[5].split(',')[0]
