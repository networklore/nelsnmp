from nelsnmp.hostinfo.version import DeviceVersion
from nelsnmp.vendors.alcatel.versions import AlcatelVersion
from nelsnmp.vendors.arista.versions import AristaVersion
from nelsnmp.vendors.cisco.versions import CiscoVersion
from nelsnmp.vendors.ericsson.versions import EricssonVersion
from nelsnmp.vendors.extreme.versions import ExtremeVersion
from nelsnmp.vendors.hpe.versions import HpeVersion
from nelsnmp.vendors.huawei.versions import HuaweiVersion
from nelsnmp.vendors.juniper.versions import JuniperVersion
from nelsnmp.vendors.metamako.versions import MetamakoVersion
from nelsnmp.vendors.synology.versions import SynologyVersion
from nelsnmp.vendors.synology.oids import SynologyOids


def get_device_version(**kwargs):

    vendor = None
    for key in kwargs:
        if key == 'vendor':
            vendor = kwargs[key]

    vendors = {}
    vendors['alcatel'] = AlcatelVersion
    vendors['arista'] = AristaVersion
    vendors['cisco'] = CiscoVersion
    vendors['ericsson'] = EricssonVersion
    vendors['extreme'] = ExtremeVersion
    vendors['hpe'] = HpeVersion
    vendors['huawei'] = HuaweiVersion
    vendors['juniper'] = JuniperVersion
    vendors['metamako'] = MetamakoVersion

    if vendor in vendors:
        return vendors[vendor](**kwargs)
    elif vendor == 'net-snmp':
        if 'snmp' in kwargs.keys():
            found_vendor = get_netsnmp_device_vendor(kwargs['snmp'])
            if found_vendor:
                if found_vendor == 'synology':
                    kwargs['vendor'] = 'synology'
                    return SynologyVersion(**kwargs)

    return DeviceVersion(**kwargs)


def get_netsnmp_device_vendor(snmp):

    s = SynologyOids()
    vartable = snmp.getnext(s.systemStatus)
    for varbind in vartable:
        for oid, value in varbind:
            if s.systemStatus in oid:
                return 'synology'
    return None
