import pytest
from nelsnmp.hostinfo.device import HostInfo


def test_hostinfo_invalid_parameter():
    with pytest.raises(ValueError):
        dev = 'Not an SnmpHandler'
        hostinfo = HostInfo(dev)
        hostinfo.get_version()
