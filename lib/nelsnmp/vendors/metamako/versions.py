from nelsnmp.hostinfo.version import DeviceVersion


class MetamakoVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'Metamako MOS' in line:
                self.os = 'mos'
                parts = line.split()
                if len(parts) > 4:
                    if parts[2] == 'release':
                        self.version = parts[3]
                        if parts[4].endswith('build'):
                            build = parts[5].split('\\')[0]
                            self.version += ' (build %s)' % build
