from nelsnmp.hostinfo.version import DeviceVersion


class HuaweiVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'VRP' in line:
                self.os = 'vrp'
