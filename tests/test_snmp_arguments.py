import pytest
from nelsnmp.errors import ArgumentError
from nelsnmp.snmp import SnmpHandler


def test_snmp_handler_v2c():
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    assert dev.version == '2c'
    assert dev.port == 161


def test_snmp_handler_v3():
    dev = SnmpHandler(
        host='1.1.1.1', version='3', username='user',
        level='authPriv', integrity='sha', privacy='aes', authkey='authpass',
        privkey='privkey')
    assert dev.version == '3'


def test_snmp_handler_wrong_version():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='4', username='user',
            level='authPriv', integrity='sha', privacy='aes', authkey='authpass',
            privkey='privkey')
