from nelsnmp.hostinfo.version import DeviceVersion

class CiscoVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'Cisco IOS Software' in line:
                self.os = 'ios'
                parts = line.split(',')
                for part in parts:
                    if 'Version' in part:
                        try:
                            self.version = part.split()[1]
                        except:
                            pass
                break
            elif 'Cisco Adaptive Security Appliance' in line:
                self.os = 'asa'
                parts = line.split()
                self.version =  parts[-1]
