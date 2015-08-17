from nelsnmp.hostinfo.version import DeviceVersion
from nelsnmp.vendors.cisco.versions import CiscoVersion
from nelsnmp.vendors.huawei.versions import HuaweiVersion


def get_device_version(**kwargs):

    vendor = None
    for key in kwargs:
        if key == 'vendor':
            vendor = kwargs[key]

    if vendor == 'cisco':
        return CiscoVersion(**kwargs)

    elif vendor == 'huawei':
        return HuaweiVersion(**kwargs)

    return DeviceVersion(**kwargs)
