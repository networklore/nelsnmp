from nelsnmp.hostinfo.version import DeviceVersion
from nelsnmp.vendors.airespace.oids import AirespaceOids


class CiscoVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'IOS-XE Software' in line:
                self.os = 'ios-xe'
                parts = line.split(',')
                for part in parts:
                    if 'Version' in part:
                        version_strings = part.split()
                        if len(version_strings) > 1:
                            self.version = version_strings[1]
                break
            elif 'Cisco IOS Software' in line:
                self.os = 'ios'
                parts = line.split(',')
                for part in parts:
                    if 'Version' in part:
                        version_strings = part.split()
                        if len(version_strings) > 1:
                            self.version = version_strings[1]
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
                        version_strings = part.split()
                        if len(version_strings) > 1:
                            self.version = version_strings[1]
                break
            elif 'Cisco NX-OS' in line:
                self.os = 'nxos'
                parts = line.split(',')
                for part in parts:
                    if 'Version' in part:
                        version_strings = part.split()
                        if len(version_strings) > 1:
                            self.version = version_strings[1]
                            break
                break
            elif line == 'Cisco Controller':
                self._get_wlc_version()

    def _get_wlc_version(self):
        o = AirespaceOids()
        vartable = self._snmp.getnext(o.agentInventoryProductVersion)
        for varbinds in vartable:
            for oid, value in varbinds:
                if o.agentInventoryProductVersion in oid:
                    self.os = 'aireos'
                    self.version = value
