import pytest
from pysnmp.proto.rfc1902 import ObjectName, OctetString
from pyasn1.type.univ import ObjectIdentifier
from test_classes import GetCmd
from nelsnmp.hostinfo.device import HostInfo
from nelsnmp.snmp import SnmpHandler


@pytest.fixture()
def declared_hostinfo(monkeypatch):
    data = [
        [ObjectName('.1.3.6.1.2.1.1.1.0'),
         OctetString('Cisco Adaptive Security Appliance Version 9.3(2)2')],
        [ObjectName('.1.3.6.1.2.1.1.2.0'),
         ObjectIdentifier('1.3.6.1.4.1.9.1.2114')],
        [ObjectName('.1.3.6.1.2.1.1.3.0'),
         OctetString('replace with uptime')],
        [ObjectName('.1.3.6.1.2.1.1.4.0'),
         OctetString('Networklore')],
        [ObjectName('.1.3.6.1.2.1.1.6.0'),
         OctetString('Westeros')],
    ]
    return GetCmd(monkeypatch, return_value=data)


@pytest.fixture()
def declared_hostinfo_unknown_vendor(monkeypatch):
    data = [
        [ObjectName('.1.3.6.1.2.1.1.2.0'),
         ObjectIdentifier('1.3.6.1.4.1.1234567.1.2114')]
    ]
    return GetCmd(monkeypatch, return_value=data)


def test_hostinfo_get_all(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_all()
    assert hostinfo.description == 'Cisco Adaptive Security Appliance Version 9.3(2)2'
    assert hostinfo.contact == 'Networklore'
    assert hostinfo.location == 'Westeros'
    assert hostinfo.vendor == 'cisco'
    assert hostinfo.version == '9.3(2)2'

def test_hostinfo_get_description(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_description()
    assert hostinfo.description == 'Cisco Adaptive Security Appliance Version 9.3(2)2'


def test_hostinfo_get_contact(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_contact()
    assert hostinfo.contact == 'Networklore'


def test_hostinfo_get_location(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_location()
    assert hostinfo.location == 'Westeros'


def test_hostinfo_get_vendor(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_vendor()
    assert hostinfo.vendor == 'cisco'


def test_hostinfo_get_vendor_unknown(declared_hostinfo_unknown_vendor):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_vendor()
    assert hostinfo.vendor == 'UNKNOWN'


def test_hostinfo_get_version(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_version()
    assert hostinfo.version == '9.3(2)2'

def test_hostinfo_get_version_known_vendor(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev, vendor='cisco')
    hostinfo.get_version()
    assert hostinfo.version == '9.3(2)2'
