from setuptools import find_packages, setup

setup(
    name="gfapi-cffi",
    version="0.1.0",
    description="Python bindings for GlusterFS libgfapi by CFFI",
    license="GPLv2 or LGPLv3+",
    author="AiPods",
    author_email="aihd-cqu@foxmail.com",
    url="http://www.gluster.org",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Filesystems",
    ],
    python_requires=">=3",
    install_requires=["cffi>=1.10.0"],
    cffi_modules=["./gfapi_cffi/libgfapi/build_cffi_libgfapi.py:ffibuilder"],
)
