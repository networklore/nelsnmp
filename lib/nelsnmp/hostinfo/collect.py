from nelsnmp.hostinfo.version import DeviceVersion
from nelsnmp.vendors.alcatel.versions import AlcatelVersion
from nelsnmp.vendors.arista.versions import AristaVersion
from nelsnmp.vendors.cisco.versions import CiscoVersion
from nelsnmp.vendors.ericsson.versions import EricssonVersion
from nelsnmp.vendors.huawei.versions import HuaweiVersion
from nelsnmp.vendors.juniper.versions import JuniperVersion
from nelsnmp.vendors.synology.versions import SynologyVersion
from nelsnmp.vendors.synology.oids import SynologyOids


def get_device_version(**kwargs):

    vendor = None
    for key in kwargs:
        if key == 'vendor':
            vendor = kwargs[key]

    if vendor == 'alcatel':
        return AlcatelVersion(**kwargs)
    if vendor == 'arista':
        return AristaVersion(**kwargs)
    if vendor == 'cisco':
        return CiscoVersion(**kwargs)
    if vendor == 'ericsson':
        return EricssonVersion(**kwargs)
    elif vendor == 'huawei':
        return HuaweiVersion(**kwargs)
    elif vendor == 'juniper':
        return JuniperVersion(**kwargs)
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
