##
## Name:     setup.py
## Purpose:  Python build and installation script for ctypes-based cURL wrapper.
##
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##

from distutils.core import setup
VERSION = '1.0'

setup(name = 'curled',
      version = VERSION,
      description = 'Interface to libcurl using ctypes',
      author = 'Michael J. Fromberger',
      classifiers = ['Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'License :: Other/Proprietary License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Internet',
                     'Topic :: Software Development :: ' \
                     'Libraries :: Python Modules'],
      packages = ['curled'],
      package_dir = {'curled': ''},
      )

# Here there be dragons
