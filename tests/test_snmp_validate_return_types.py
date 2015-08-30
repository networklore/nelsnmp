import pytest
from pyasn1.type.univ import ObjectIdentifier
from test_classes import GetCmdValues
from nelsnmp.snmp import SnmpHandler
from pysnmp.proto.rfc1902 import (
    Counter32,
    Counter64,
    Gauge32,
    Integer,
    Integer32,
    IpAddress,
    ObjectName,
    OctetString,
    TimeTicks,
    Unsigned32,
)

data = []
data.append([ObjectName('.1.'), Counter32('100'), 100])
data.append([ObjectName('.1.'), Counter64('100'), 100])
data.append([ObjectName('.1.'), Gauge32('100'), 100])
data.append([ObjectName('.1.'), Integer('100'), 100])
data.append([ObjectName('.1.'), Integer32('100'), 100])
data.append([ObjectName('.1.'), IpAddress('192.168.1.1'), '192.168.1.1'])
data.append([ObjectName('.1.'), ObjectIdentifier('1'), '1'])
data.append([ObjectName('.1.'), OctetString('my_string'), 'my_string'])
data.append([ObjectName('.1.'), Unsigned32('100'), 100])


@pytest.fixture(scope='function', params=data)
def query_data(monkeypatch, request):
    snmp_data = [[request.param[0], request.param[1]]]
    return GetCmdValues(
        monkeypatch,
        return_value=snmp_data,
        params=request.param
    )


def test_return_value_types(query_data):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    varbinds = dev.get('1')
    for oid, value in varbinds:
        assert value == query_data.value
