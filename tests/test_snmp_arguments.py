from nelsnmp.snmp import SnmpHandler


def test_snmp_handler_v2c():
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    assert dev.version == '2c'
    assert dev.port == 161


def test_arg_non_default_port():
    dev = SnmpHandler(
        host='1.1.1.1',
        version='2c',
        community='public',
        port=35000)
    assert dev.version == '2c'
    assert dev.port == 35000


def test_snmp_handler_v3_authpriv():
    dev = SnmpHandler(
        host='1.1.1.1', version='3', username='user',
        level='authPriv', integrity='sha', privacy='aes', authkey='authpass',
        privkey='privkey')
    assert dev.version == '3'


def test_snmp_handler_v3_authnopriv():
    dev = SnmpHandler(
        host='1.1.1.1', version='3', username='user',
        level='authNoPriv', integrity='sha', authkey='authpass')
    assert dev.version == '3'
    assert dev.authkey == 'authpass'
