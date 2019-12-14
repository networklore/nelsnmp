from nelsnmp.hostinfo.version import DeviceVersion


class ExtremeVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'ExtremeXOS' in line:
                self.os = 'extremexos'
                parts = line.split()
                if len(parts) > 4:
                    if parts[2] == 'version':
                        self.version = '{} {}'.format(parts[3], parts[4])

