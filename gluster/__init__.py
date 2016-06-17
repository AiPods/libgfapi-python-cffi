# Copyright (c) 2016 Red Hat, Inc.
#
# This file is part of libgfapi-python project which is a
# subproject of GlusterFS ( www.gluster.org)
#
# This file is licensed to you under your choice of the GNU Lesser
# General Public License, version 3 or any later version (LGPLv3 or
# later), or the GNU General Public License, version 2 (GPLv2), in all
# cases as published by the Free Software Foundation.

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)


class PkgInfo(object):
    def __init__(self, canonical_version, release, name, final):
        self.canonical_version = canonical_version
        self.release = release
        self.name = name
        self.final = final

    def save_config(self, filename):
        """
        Creates a file with the package configuration which can be sourced by
        a bash script.
        """
        with open(filename, 'w') as fd:
            fd.write("NAME=%s\n" % self.name)
            fd.write("VERSION=%s\n" % self.canonical_version)
            fd.write("RELEASE=%s\n" % self.release)

    @property
    def pretty_version(self):
        if self.final:
            return self.canonical_version
        else:
            return '%s-dev' % (self.canonical_version,)


# Change the Package version here
_pkginfo = PkgInfo('0.0.1', '0', 'python-libgfapi', False)
__version__ = _pkginfo.pretty_version
__canonical_version__ = _pkginfo.canonical_version
