from nelsnmp.snmp import is_ipv4_address


def test_is_valid_ip():
    assert is_ipv4_address('172.27.9.64')


def test_is_not_valid_ip():
    assert not is_ipv4_address('172.27.9.640')
