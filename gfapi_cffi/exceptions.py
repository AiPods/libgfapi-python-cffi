
class LibgfapiException(Exception):
    pass


class VolumeNotMounted(LibgfapiException):
    pass


class Error(EnvironmentError):
    pass
