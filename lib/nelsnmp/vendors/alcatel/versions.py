from nelsnmp.hostinfo.version import DeviceVersion


class AlcatelVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'TiMOS' in line:
                self.os = 'timos'
                parts = line.split()
                if parts[0][:6] == 'TiMOS-':
                    version_parts = parts[0].split('-')
                    if len(version_parts) == 3:
                        self.version = version_parts[2]
