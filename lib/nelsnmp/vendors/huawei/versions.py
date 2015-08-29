from nelsnmp.hostinfo.version import DeviceVersion


class HuaweiVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'VRP' in line:
                self.os = 'vrp'
                parts = line.split()
                if len(parts) > 5:
                    if parts[2][-7:] == 'Version':
                        self.version = parts[3]
                        if parts[5].endswith(')'):
                            if self.version:
                                self.version += ' - ' + parts[5][:-1]
