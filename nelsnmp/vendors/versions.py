
class DeviceVersion(object):

    def __init__(self, **kwargs):

        self._sysobjectid = None
        self._description = None
        self._descriptions = []
        self.device_class = None
        self.os = None
        self.version = None

        for key in kwargs:
            if key == 'sysobjectid':
                self._sysobjectid = kwargs[key]
            if key == 'description':
                self._description = kwargs[key]
                self._descriptions = kwargs[key].split('\r\n')

        self._get_version()
        self._clean()

    def _get_version(self):
        pass

    def _clean(self):
        if self.version == None:
            self.version == 'UNKNOWN'
