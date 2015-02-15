from pysnmp.entity.rfc3413.oneliner import cmdgen

SNMP_VERSIONS = ('2c', '3')

class SnmpHandler(object):
    

    def __init__(self, **kwargs):

        self.port = 161
        self.version = False
        self.community = False
        self.host = False


        for key in kwargs:
            print key, kwargs[key]
            if key == 'version' and kwargs[key] in SNMP_VERSIONS:   
                self.version = kwargs[key]
            if key == 'community':
                self.community = kwargs[key]

        if self.version == False or self.host == False:
            print "You have to set version and host"

