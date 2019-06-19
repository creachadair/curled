##
## Name:     lctypes.py
## Purpose:  FFI type signatures for libcurl interface.
##
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##

from ctypes import (
    c_void_p,
    c_int,
    c_int64,
    c_char_p,
    c_long,
    c_size_t,
    c_uint,
    c_double,
    POINTER,
    CFUNCTYPE,
    Structure,
)

# Library types used in <curl/curl.h>
CURL = c_void_p
CURLM = c_void_p
CURLINFO = c_int
CURLcode = c_int
CURLoption = c_int
CURLversion = c_int
curl_infotype = c_int
curl_value_t = c_int64
curl_null = 0  # Use "None" for pointer types
curl_off_t = c_int64


class curl_version_info_data(Structure):
    _fields_ = [
        ('age', CURLversion),  # age of the returned struct
        ('version', c_char_p),  # LIBCURL_VERSION
        ('version_num', c_uint),  # LIBCURL_VERSION_NUM
        ('host', c_char_p),  # OS/host/cpu/machine when configured
        ('features', c_int),  # bitmask, see CURL_VERSION_* constants
        ('ssl_version', c_char_p),  # human-readable string
        ('ssl_version_num', c_long),  # not used anymore, always 0
        ('libz_version', c_char_p),  # human-readable string
        ('protocols', POINTER(c_char_p)),  # terminated by a NULL entry
        ('ares', c_char_p),
        ('ares_num', c_int),
        ('libidn', c_char_p),
        ('iconv_ver_num', c_int),
        ('libssh_version', c_char_p),  # human-readable string
    ]


class curl_slist(Structure):
    pass


curl_slist._fields_ = [
    ('data', c_char_p),
    ('next', POINTER(curl_slist)),
]


def type_setter(restype, *argtypes):

    def f(funcptr):
        funcptr.restype = restype
        funcptr.argtypes = argtypes
        return funcptr

    return f


func_type_map = dict(
    curl_easy_cleanup=type_setter(None, CURL),
    curl_easy_duphandle=type_setter(CURL, CURL),
    curl_easy_getinfo=type_setter(CURLcode, CURL, CURLINFO, c_void_p),
    curl_easy_init=type_setter(CURL),
    curl_easy_pause=type_setter(CURLcode, CURL, c_int),
    curl_easy_perform=type_setter(CURLcode, CURL),
    curl_easy_recv=type_setter(CURLcode, CURL, c_void_p, c_size_t),
    curl_easy_reset=type_setter(None, CURL),
    curl_easy_send=type_setter(CURLcode, CURL, c_void_p, c_size_t,
                               POINTER(c_size_t)),
    curl_easy_setopt=type_setter(CURLcode, CURL, CURL, curl_value_t),
    curl_easy_strerror=type_setter(c_char_p, CURLcode),
    curl_easy_unescape=type_setter(c_char_p, CURL, c_char_p, c_int,
                                   POINTER(c_int)),
    curl_free=type_setter(None, c_char_p),
    curl_global_cleanup=type_setter(None),
    curl_global_init=type_setter(CURLcode, c_long),
    curl_version=type_setter(c_char_p),

    # Note: These two functions actually return a pointer to a structure,
    # but ctypes doesn't permit callbacks to have compound return types.
    # The caller must therefore cast the pointer back manually. :P
    curl_version_info=type_setter(c_void_p, CURLversion),
    curl_slist_append=type_setter(c_void_p, POINTER(curl_slist), c_char_p),
    curl_slist_free_all=type_setter(None, POINTER(curl_slist)),
)

# Generic interface for reading and writing data, like fread/fwrite
# size_t callback(void *buf, size_t size, size_t count, void *userdata)
data_callback_t = CFUNCTYPE(c_size_t, c_void_p, c_size_t, c_size_t, c_void_p)

# For CURLOPT_WRITEFUNCTION
curl_writefunc_t = data_callback_t

# For CURLOPT_READFUNCTION
curl_readfunc_t = data_callback_t

# For CURLOPT_SEEKFUNCTION
# int sf(void *stream, curl_off_t offset, int origin)
curl_seekfunc_t = CFUNCTYPE(c_int, c_void_p, curl_off_t, c_int)

# For CURLOPT_PROGRESSFUNCTION
# int pf(void *handle, double dltotal, double dlnow, double ultotal, double ulnow)
curl_progfunc_t = CFUNCTYPE(c_int, c_void_p, c_double, c_double, c_double,
                            c_double)

# For CURLOPT_HEADERFUNCTION
curl_headfunc_t = data_callback_t

# For CURLOPT_DEBUGFUNCTION
# int df(CURL *ch, curl_infotype t, char *data, size_t size, void *userdata)
curl_debugfunc_t = CFUNCTYPE(c_int, curl_infotype, c_char_p, c_size_t, c_void_p)

__all__ = (
    # Basic library types
    'CURL',
    'CURLM',
    'CURLINFO',
    'CURLcode',
    'CURLoption',
    'CURLversion',
    'curl_infotype',
    'curl_value_t',
    'curl_null',
    'curl_off_t',

    # Structures
    'curl_version_info_data',
    'curl_slist',

    # Callback type signatures
    'curl_writefunc_t',
    'curl_readfunc_t',
    'curl_seekfunc_t',
    'curl_progfunc_t',
    'curl_headfunc_t',
    'curl_debugfunc_t',

    # Function type signatures
    'func_type_map',
)

# Here there be dragons
