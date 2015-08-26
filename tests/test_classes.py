from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import ObjectName, OctetString


class GetCmd:
    def __init__(self, monkeypatch, return_value=None):
        global get_snmpdata
        get_snmpdata = self._get_snmpdata
        self.return_value = return_value
        monkeypatch.setattr(cmdgen.CommandGenerator, 'getCmd', self.mygetcmd)

    def _get_snmpdata(self, *snmp_data):
        if self.return_value:
            return self.return_value
        else:
            for snmp in snmp_data:
                dat = snmp
            snmpdata = [[ObjectName('1.1'), OctetString(dat)]]
            return snmpdata

    def mygetcmd(snmp_auth, transport, *snmp_data):
        snmpdata = get_snmpdata(*snmp_data)
        return None, None, None, snmpdata
