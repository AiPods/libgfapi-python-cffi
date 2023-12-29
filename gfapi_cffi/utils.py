import errno
import os
from functools import wraps

from .exceptions import VolumeNotMounted


def validate_mount(func):
    """
    Decorator to assert that volume is initialized and mounted before any
    further I/O calls are invoked by methods.

    :param func: method to be decorated and checked.
    """
    def _exception(volname):
        raise VolumeNotMounted('Volume "%s" not mounted.' % (volname))

    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        if self.fs and self._mounted:
            return func(*args, **kwargs)
        else:
            return _exception(self.volname)
    wrapper.__wrapped__ = func

    return wrapper


def validate_glfd(func):
    """
    Decorator to assert that glfd is valid.

    :param func: method to be decorated and checked.
    """
    def _exception():
        raise OSError(errno.EBADF, os.strerror(errno.EBADF))

    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        if self.fd:
            return func(*args, **kwargs)
        else:
            return _exception()
    wrapper.__wrapped__ = func

    return wrapper
