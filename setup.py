from setuptools import setup, find_packages
from distutils.command.install import install as _install

import sys
import platform

if not sys.version_info[0] == 2:
	print "Sorry, Python 3 is not supported (yet)"
	exit()

if sys.version_info[0] == 2 and sys.version_info[1] < 6:
	print "Sorry, Python < 2.6 is not supported"
	exit()

req_lines = []
install_reqs = []

long_description = ""

setup(name='neteasy',
	  version='0.0.1',
	  description="",
	  long_description=long_description,
	  author="maoyw",
	  author_email="838662311@qq.com",
	  url="https://github.com/davidsome",
	  packages=find_packages("."),
	  install_requires=install_reqs,
	  license="Apache License 2.0",
	  platforms=["Posix; OS X; Windows"],
	  keywords=('neteasy'),
	  classifiers=[
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
	  ]
	  )