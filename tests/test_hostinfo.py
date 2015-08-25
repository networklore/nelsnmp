import pytest
import nelsnmp.snmp
from nelsnmp.hostinfo.collect import get_device_version
from nelsnmp.hostinfo.device import HostInfo
from nelsnmp.snmp import SnmpHandler


@pytest.fixture
def patch_snmp_getnext(monkeypatch):

    # Testing with monkeypatch

    def mygetnext(*junk):
        return [['sd', 'df']]

    monkeypatch.setattr(nelsnmp.snmp.SnmpHandler, 'getnext', mygetnext)


def test_os():
    hostinfo = get_device_version(
        sysobjectid='random',
        description='Cisco IOS Software, catalyst, Version 15.x, RELEASE',
        vendor='cisco')
    assert hostinfo.os == 'ios'


def test_hostinfo():
    handler = SnmpHandler(host='1.1.1.1')
    hostinfo = HostInfo(handler)
    assert hostinfo.os is None


def test_hostinfo_cisco_ios_version():
    handler = SnmpHandler(host='1.1.1.1')
    hostinfo = HostInfo(
        handler,
        vendor='cisco',
        description='Cisco IOS Software, catalyst, Version 15.x, RELEASE')
    hostinfo.get_version()
    assert hostinfo.version == '15.x'


def test_hostinfo_netsnmp(patch_snmp_getnext):
    handler = SnmpHandler(host='1.1.1.1')
    hostinfo = HostInfo(
        handler,
        vendor='net-snmp',
        description='Cisco IOS Software, catalyst, Version 15.x, RELEASE')
    hostinfo.get_version()
    assert hostinfo.version == 'UNKNOWN'
