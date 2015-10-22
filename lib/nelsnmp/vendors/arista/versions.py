from nelsnmp.hostinfo.version import DeviceVersion


class AristaVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'Arista Networks EOS' in line:
                self.os = 'eos'
                parts = line.split()
                if len(parts) > 4:
                    if parts[3] == 'version':
                        self.version = parts[4]
