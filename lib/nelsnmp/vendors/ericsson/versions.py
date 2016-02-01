from nelsnmp.hostinfo.version import DeviceVersion


class EricssonVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'Redback Networks SmartEdge OS' in line:
                self.os = 'seos'
                parts = line.split()
                if len(parts) > 5:
                    if parts[4] == 'Version':
                        version_parts = parts[5].split('-')
                        if len(version_parts) > 2:
                            self.version = version_parts[1]
