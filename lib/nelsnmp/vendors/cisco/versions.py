from nelsnmp.hostinfo.version import DeviceVersion


class CiscoVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'IOS-XE Software' in line:
                self.os = 'ios-xe'
                parts = line.split(',')
                for part in parts:
                    if 'Version' in part:
                        try:
                            self.version = part.split()[1]
                        except:
                            pass
                break
            elif 'Cisco IOS Software' in line:
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
                self.version = parts[-1]
            elif 'Cisco IOS XR Software' in line:
                self.os = 'ios-xr'
                parts = line.split(',')
                for part in parts:
                    if 'Version' in part:
                        try:
                            self.version = part.split()[1]
                        except:
                            pass
                break
            elif 'Cisco NX-OS' in line:
                self.os = 'nxos'
                parts = line.split(',')
                for part in parts:
                    if 'Version' in part:
                        try:
                            self.version = part.split()[1]
                            break
                        except:
                            pass
                break
