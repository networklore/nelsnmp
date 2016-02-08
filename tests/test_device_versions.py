import glob
import pytest
import yaml
from pysnmp.proto.rfc1902 import ObjectName, OctetString
from pyasn1.type.univ import ObjectIdentifier
from test_classes import GetCmd
from nelsnmp.hostinfo.device import HostInfo
from nelsnmp.snmp import SnmpHandler


input_files = glob.glob('tests/valid_hostinfo_files/*.yml')
input_devices = []

for input_file in input_files:
    with open(input_file, 'r') as f:
        device_declarations = yaml.load(f.read())
    for key in device_declarations.keys():
        input_devices.append(device_declarations[key])


@pytest.fixture(scope='function', params=input_devices)
def declared_hostinfo(monkeypatch, request):
    data = [
        [ObjectName('.1.3.6.1.2.1.1.2.0'),
         ObjectIdentifier(request.param['sysobjectid'])],
        [ObjectName('.1.3.6.1.2.1.1.1.0'),
         OctetString(request.param['description'])]
    ]
    get_oids = request.param.get('get_oids')
    if get_oids:
        for entry in get_oids:
            data.append([ObjectName(get_oids[entry]['oid']),
                        OctetString(get_oids[entry]['value'])])

    if 'walk_oids' in request.param.keys():
        get_next_return = []
        for extra_oid in request.param['walk_oids']:
            get_next_return.append([ObjectName('.' + request.param['walk_oids'][extra_oid]['oid']),
                OctetString(request.param['walk_oids'][extra_oid]['value'])])
        walk_data = [get_next_return]
    else:
        walk_data = None
    return GetCmd(monkeypatch, return_value=data, walk_data=walk_data, params=request.param)


def test_device_versions(declared_hostinfo):
    dev = SnmpHandler(host='1.1.1.1', version='2c', community='public')
    hostinfo = HostInfo(dev)
    hostinfo.get_version()
    assert hostinfo.vendor == declared_hostinfo.vendor
    assert hostinfo.os == declared_hostinfo.os
    assert hostinfo.version == declared_hostinfo.version
