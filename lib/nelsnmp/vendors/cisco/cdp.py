from nelsnmp.snmp import SnmpHandler
from nelsnmp.vendors.cisco.oids import CiscoOids
o = CiscoOids()


class CdpNeighbors(object):
    def __init__(self, snmp=None):
        if not isinstance(snmp, SnmpHandler):
            raise ValueError('Must pass a Nelmon SnmpHandler')
        self._snmp = snmp
        self._raw_data = {}
        self.interface = {}

    def _get_interface_names(self):
        cdp_interfaces = []
        for interface in self._raw_data['neighbor_interfaces']:
            cdp_interfaces.append('%s.%s' % (o.ifDescr, interface))
        varbinds = self._snmp.get(*cdp_interfaces)
        for oid, value in varbinds:
            interface = oid.split('.')[-1]
            self.interface[interface] = value

    def _get_neighbors_data(self):
        vartable = self._snmp.getnext(o.cdpCacheEntry)
        neighbors = {}
        local_cdp_interfaces = []
        for varbind in vartable:
            for oid, value in varbind:
                entry = oid.rsplit('.', 2)[-1]
                interface = oid.rsplit('.', 2)[-2]
                if entry not in neighbors.keys():
                    neighbors[entry] = {}
                if interface not in local_cdp_interfaces:
                    local_cdp_interfaces.append(interface)
                if interface not in neighbors[entry].keys():
                    neighbors[entry][interface] = {}
                if o.cdpCacheDeviceId in oid:
                    neighbors[entry][interface]['cdpCacheDeviceId'] = value
                if o.cdpCacheDevicePort in oid:
                    neighbors[entry][interface]['cdpCacheDevicePort'] = value
        self._raw_data['neighbors'] = neighbors
        self._raw_data['neighbor_interfaces'] = local_cdp_interfaces
        self._get_interface_names()

    def get_cdp_neighbors_dict(self):
        self._get_neighbors_data()
        cdp = {}
        neighbors = self._raw_data['neighbors']
        for entry in neighbors:
            for interface in neighbors[entry]:
                if_name = self.interface[interface]
                neighbor_host = neighbors[entry][interface]['cdpCacheDeviceId']
                if if_name not in cdp.keys():
                    cdp[if_name] = {}
                if neighbor_host not in cdp[if_name].keys():
                    cdp[if_name][neighbor_host] = {}
                cdp[if_name][neighbor_host]['interface'] = neighbors[entry][interface]['cdpCacheDevicePort']
        self.neighbors = cdp

    def get_cdp_neighbors_list(self):
        self._get_neighbors_data()
        cdp = {}
        neighbors = self._raw_data['neighbors']
        for entry in neighbors:
            for interface in neighbors[entry]:
                if_name = self.interface[interface]
                neighbor_host = neighbors[entry][interface]['cdpCacheDeviceId']
                if if_name not in cdp.keys():
                    cdp[if_name] = []
                data = {}
                data['neighbor'] = neighbor_host
                data['interface'] = neighbors[entry][interface]['cdpCacheDevicePort']
                cdp[if_name].append(data)
        self.neighbors = cdp
