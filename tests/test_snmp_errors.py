from nelsnmp.snmp import SnmpHandler
from nelsnmp.errors import ArgumentError, SnmpError
from nelsnmp.oids import GeneralOids


def test_handle_snmp_handler_invalid_version():
    try:
        dev = SnmpHandler(
            host='1.1.1.1', version='4', username='user',
            level='authPriv', integrity='sha', privacy='aes',
            authkey='authpass', privkey='privkey')
    except ArgumentError as e:
        assert e.__str__() == "'No valid SNMP version defined'"


# def test_non_working_snmp_get():
#    dev = SnmpHandler(host='169.254.12.18', version='2c',
#                      community='bound_to_fail')
#    o = GeneralOids()
#    try:
#        data = dev.get(o.sysDescr)
#    except SnmpError as e:
#        assert e.__str__() == "'No SNMP response received before timeout'"
