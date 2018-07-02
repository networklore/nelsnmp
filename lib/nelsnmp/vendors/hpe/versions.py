from nelsnmp.hostinfo.version import DeviceVersion


class HpeVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if (('Aruba' in line and "Switch" in line) or 'revision KB.16.04.' in line):
                self.os = 'arubaos-switch'
                parts = line.split()
                if len(parts) > 6:
                    if parts[4] == 'revision':
                        self.version = parts[5].split(',')[0]
