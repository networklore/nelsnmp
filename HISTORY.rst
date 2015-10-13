.. :changelog:

Release History
---------------

0.2.3
+++++

* Fix to handle changed return values from pysnmp 4.3.0

0.2.2
+++++

* Changes to how Synology NAS versions are reported

0.2.1
+++++

* Renamed HostInfo class
* Added IOS-XR, IOS-XE, Cisco AireOS (WLC) support to HostInfo
* Added Synology NAS support to HostInfo
* Added Huawei VRP support to HostInfo
* Added Alcatel Timos support to HostInfo
* Added product version oid from AIRESPACE-SWITCHING-MIB

0.2.0
+++++

* Added table oids from CISCO-ENVMON-MIB

0.1.9
+++++

* Added oids from CISCO-RTTMON-MIB

0.1.8
+++++

Internal structure changes. All vendor features should be created under nelsnmp.vendors.

* Implemented Hostinfo check to get vendor and version (for Cisco devices)
* Marked nelsnmp.cisco_oids as deprecated, use nelsnmp.vendors.cisco.oids
* Added sysORTable
* Added oids from CISCO-ENVMON-MIB and CISCO-ENTITY-SENSOR-MIB

0.1.7
+++++

* Made error handling more flexible

0.1.6
+++++

* Added oids from CISCO-CONFIG-COPY-MIB

0.1.5
+++++

* Added ability to set snmp port
* Added cdpCacheDeviceId, cdpCacheDevicePort

0.1.4
+++++

Created changes file
