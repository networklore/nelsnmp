import pytest
from pysnmp.entity.rfc3413.oneliner import cmdgen
import nelsnmp.snmp
from nelsnmp.hostinfo.collect import get_device_version
from nelsnmp.hostinfo.device import HostInfo
from nelsnmp.snmp import SnmpHandler
from pysnmp.proto.rfc1902 import ObjectName, OctetString
from pyasn1.type.univ import ObjectIdentifier
from test_classes import GetCmd


@pytest.fixture
def doesitwork(monkeypatch):
    return GetCmd(monkeypatch)


@pytest.fixture
def sysobject(monkeypatch):
    data = [[ObjectName('.1.3.6.1.2.1.1.2.0'), ObjectIdentifier('1.3.6.1.4.1.9.1')]]
    return GetCmd(monkeypatch, return_value=data)


@pytest.fixture
def patch_pysnmp_get(monkeypatch):
    # getCmd
    def mygetcmd(*junk):
        return None, None, None, [[ObjectName('1.1'), OctetString('b')]]
    monkeypatch.setattr(cmdgen.CommandGenerator, 'getCmd', mygetcmd)


@pytest.fixture
def snmp_val(request):
    return 'b'


@pytest.fixture
def patch_pysnmp_getnext(monkeypatch):
    # nextCmd
    def mynextcmd(*junk):
        return None, None, None, [[[ObjectName('1.1'), OctetString('b')]]]

    monkeypatch.setattr(cmdgen.CommandGenerator, 'nextCmd', mynextcmd)


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


def test_hostinfo_pysnmp_netsnmp(patch_pysnmp_getnext):
    handler = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(
        handler,
        vendor='net-snmp',
        description='Cisco IOS Software, catalyst, Version 15.x, RELEASE')
    hostinfo.get_version()
    assert hostinfo.version == 'UNKNOWN'


def test_hostinfo_pysnmp_get(patch_pysnmp_get, snmp_val):
    handler = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    data = handler.get_value('1.1')
    assert data == snmp_val


def test_fixturet(doesitwork):
    handler = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    data = handler.get_value('1.1')
    assert data == '1.1'


def test_hostinfo_get_vendor(sysobject):
    handler = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(handler)
    hostinfo.get_vendor()
    assert hostinfo.vendor == 'cisco'
