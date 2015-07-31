from nelsnmp.hostinfo.collect import get_device_version
from nelsnmp.oids import GeneralOids
from nelsnmp.snmp import SnmpHandler
from nelsnmp.vendors.mappings import vendor_map
o = GeneralOids()

class Hostinfo(object):

    def __init__(self, Snmp):

        if not isinstance(Snmp, SnmpHandler):
            raise ValueError('Must pass a Nelmon SnmpHandler')

        self.contact = None
        self.location = None
        self.sysobjectid = None
        self.description = None
        self.os = None
        self.vendor = None
        self.version = None
        self.uptime = None
        self._snmp = Snmp

    def _parse_data(self, data):
        for oid, value in data:
            if o.sysContact in oid:
                self.contact = value
            if o.sysDescr in oid:
                self.description = value
            if o.sysLocation in oid:
                self.location = value
            if o.sysObjectId in oid:
                self.sysobjectid = value
            if o.sysUpTime in oid:
                self.uptime = value


    def get_all(self):
        oids = [
            o.sysContact + '.0',
            o.sysDescr + '.0',
            o.sysLocation + '.0',
            o.sysObjectId + '.0',
            o.sysUpTime + '.0',
        ]
        data = self._snmp.get(*oids)
        self._parse_data(data)
        self.get_vendor()
        self.get_version()

    def get_description(self):
        data = self._snmp.get(o.sysDescr + '.0')
        self._parse_data(data)

    def get_contact(self):
        data = self._snmp.get(o.sysContact + '.0')
        self._parse_data(data)

    def get_location(self):
        data = self._snmp.get(o.sysLocation + '.0')
        self._parse_data(data)

    def get_vendor(self):
        if self.sysobjectid == None:
            self.get_sysobjectid()
        try:
            enterprise_id = self.sysobjectid.split('.')[6]
            self.vendor = vendor_map[enterprise_id]
        except:
            self.vendor = 'UNKNOWN'

    def get_version(self):
        if self.vendor == None:
            self.get_vendor()
        if self.description == None:
            self.get_description()
        version_info = get_device_version(
            sysobjectid=self.sysobjectid,
            description=self.description,
            vendor=self.vendor
        )
        self.os = version_info.os
        self.version = version_info.version

    def get_sysobjectid(self):
        data = self._snmp.get(o.sysObjectId + '.0')
        self._parse_data(data)
