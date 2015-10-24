import pytest
from nelsnmp.errors import ArgumentError
from nelsnmp.snmp import SnmpHandler


def test_snmp_missing_host():
    with pytest.raises(ArgumentError):
        SnmpHandler(version='2c', community='public')


def test_snmp_handler_invalid_version():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='4', username='user',
            level='authPriv', integrity='sha', privacy='aes',
            authkey='authpass', privkey='privkey')


def test_snmp_arg_invalid_port_type():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', integrity='sha', privacy='aes',
            authkey='authpass', privkey='privkey', port='five')


def test_snmp_arg_invalid_port_number():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', integrity='sha', privacy='aes',
            authkey='authpass', privkey='privkey', port=65536)


def test_snmpv3_arg_missing_user():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3',
            level='authPriv', integrity='sha', privacy='aes',
            authkey='authpass', privkey='privkey', port=65532)


def test_snmpv3_arg_missing_level():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            integrity='sha', privacy='aes',
            authkey='authpass', privkey='privkey')


def test_snmp_arg_missing_integrity():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', privacy='aes',
            authkey='authpass', privkey='privkey', port=65532)


def test_snmp_arg_missing_privacy():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', integrity='sha',
            authkey='authpass', privkey='privkey', port=65532)


def test_snmp_arg_missing_authkey():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', privacy='aes', integrity='sha',
            privkey='privkey', port=65532)


def test_snmp_arg_missing_privkey():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', privacy='aes', integrity='sha',
            authkey='authpass', port=65532)


def test_snmp_arg_invalid_level():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='secret', integrity='sha', privacy='aes',
            authkey='authpass', privkey='privkey', port=65532)


def test_snmp_arg_invalid_integrity():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', integrity='sha123', privacy='aes',
            authkey='authpass', privkey='privkey', port=65532)


def test_snmp_arg_invalid_privacy():
    with pytest.raises(ArgumentError):
        SnmpHandler(
            host='1.1.1.1', version='3', username='user',
            level='authPriv', integrity='sha', privacy='aes123',
            authkey='authpass', privkey='privkey', port=65532)
