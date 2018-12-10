##
## Name:     __init__.py
## Purpose:  Interface to libcurl based on ctypes.
##
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##
## Basic usage examples
##
##   import curled, curled.constants as const
##   curl = curled.Curl()
##   curl.setopt(const.CURLOPT_URL, 'http://www.google.com/')
##   curl.setopt(const.CURLOPT_VERBOSE, True)
##   curl.setopt(const.CURLOPT_FOLLOWLOCATION, True)
##   curl.setopt(const.CURLOPT_MAXREDIRS, 5)
##   curl.perform()
##
##   print("%.2f sec. from %s" % (
##     curl.getinfo(const.CURLINFO_TOTAL_TIME),
##     curl.getinfo(const.CURLINFO_EFFECTIVE_URL)))
##
##   curl.reset()
##
## Symbolic constants are defined in the "constants" submodule.  Their
## names and values were extracted mechanically from <curl/curl.h>.
##
from __future__ import absolute_import

from . import constants, util
from .objects import *

__all__ = (
    'constants',
    'util',
    'CURLError',
    'CURLVersionError',
    'Curl',
)

# Here there be dragons
