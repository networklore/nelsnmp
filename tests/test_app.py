

import nelsnmp
import nelsnmp.snmp
from nelsnmp.hostinfo.collect import get_device_version


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_os():
    hostinfo = get_device_version(
        sysobjectid='random',
        description='Cisco IOS Software, catalyst, Version 15.x, RELEASE',
        vendor='cisco')
    assert hostinfo.os == 'ios'
