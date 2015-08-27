from nelsnmp.vendors.airespace.oids import AirespaceOids
from nelsnmp.vendors.cisco.oids import CiscoOids
from nelsnmp.vendors.synology.oids import SynologyOids
from nelsnmp.cisco_oids import CiscoOids as OldCiscoOids

def test_airespace_oids_not_broken():
    o = AirespaceOids()
    assert o.agentInventoryProductVersion == '1.3.6.1.4.1.14179.1.1.1.14'


def test_cisco_oids_not_broken():
    o = CiscoOids()
    assert o.cdpGlobalRun == '1.3.6.1.4.1.9.9.23.1.3.1'


def test_old_cisco_oids_not_broken():
    o = OldCiscoOids()
    assert o.cdpGlobalRun == '1.3.6.1.4.1.9.9.23.1.3.1'


def test_synology_oids_not_broken():
    o = SynologyOids()
    assert o.synoSystem == '1.3.6.1.4.1.6574.1'
