libgfapi-python-cffi
=======

This is an alternative project for [libgfapi-python](https://github.com/gluster/libgfapi-python) .

Issues with libgfapi-python
------
 - Many issues in aarch64
 - Only support GlusterFS < 3.7

What's new with libgfapi-python-cffi
------
 - Use CFFI rewrite libgfapi-python
 - Support aarch64
 - Support GlusterFS >= 6.0

Requires:
------
 - glusterfs-api-devel >= 6.0
 - python-devel >= 3.6
 - python-cffi >= 1.10.0
 - gcc ...

Build:
------
 - python setup.py bdist_wheel