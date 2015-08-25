

class DeviceVersion(object):

    def __init__(self, **kwargs):

        self._sysobjectid = None
        self._description = None
        self._descriptions = []
        self.device_class = None
        self.os = None
        self.version = None
        self.vendor = None

        for key in kwargs:
            if key == 'sysobjectid':
                self._sysobjectid = kwargs[key]
            elif key == 'description':
                self._description = kwargs[key]
                self._descriptions = kwargs[key].split('\r\n')
            elif key == 'snmp':
                self._snmp = kwargs[key]
            elif key == 'vendor':
                self.vendor = kwargs[key]

        self._get_version()
        self._clean()

    def _get_version(self):
        pass

    def _clean(self):
        if self.os is None:
            self.os = 'UNKNOWN'
        if self.version is None:
            self.version = 'UNKNOWN'
