import pytest
from test_classes import SetCmd
from nelsnmp.snmp import SnmpHandler


@pytest.fixture(scope='function')
def set_data(monkeypatch, request):
    return SetCmd(monkeypatch)


# Use params instead or move to function to test data types
def test_snmp_set_string(set_data):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    try:
        dev.set('1', 'ab')
        success = True
    except:
        success = False

    assert success


def test_snmp_set_int(set_data):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    try:
        dev.set('1', 1)
        success = True
    except:
        success = False

    assert success


def test_snmp_set_float(set_data):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    try:
        dev.set('1', 1.1)
        success = True
    except:
        success = False

    assert success


def test_snmp_set_address(set_data):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    try:
        dev.set('1', '1.1.1.1')
        success = True
    except:
        success = False

    assert success
