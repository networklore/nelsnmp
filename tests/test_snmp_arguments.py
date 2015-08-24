

import nelsnmp
from nelsnmp.snmp import SnmpHandler
from nelsnmp.hostinfo.collect import get_device_version


def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5


def test_snmp_handler_v2c():
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    assert dev.version == '2c'


def test_snmp_handler_v3():
    dev = SnmpHandler(host='1.1.1.1', version='3', username='user',
        level='authPriv', integrity='sha', privacy='aes', authkey='authpass',
        privkey='privkey')
    assert dev.version == '3'


def test_os():
    hostinfo = get_device_version(
        sysobjectid='random',
        description='Cisco IOS Software, catalyst, Version 15.x, RELEASE',
        vendor='cisco')
    assert hostinfo.os == 'ios'
