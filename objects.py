##
## Name:     objects.py
## Purpose:  Core objects for ctypes-based libcurl interface.
##
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##
from __future__ import absolute_import

import atexit, ctypes, ctypes.util, os
from . import constants, options
from .lctypes import *

# Default location to look for libcurl
LIBCURL_LIBRARY_PATH = os.getenv('LIBCURL_LIBRARY_PATH', None)

try:
    unicode = unicode  # Works in Python 2, fails in 3.
except NameError:
    unicode = str


class CURLError(Exception):
    pass


class CURLVersionError(CURLError):
    """Indicates the library is too old for the requested operation.
    """
    pass


class CurlBase(object):
    """High-level interface to libcurl.
    """
    libcurl_path = None
    libcurl_dll = None

    @classmethod
    def ENC(cls, obj):
        if isinstance(obj, unicode): return obj.encode('utf8')
        else: return obj

    @classmethod
    def DEC(cls, obj):
        if isinstance(obj, bytes): return obj.decode('utf8')
        else: return obj

    @classmethod
    def load_library(cls, path):
        """Load and populate a libcurl_base object from the library
        stored in the specified path.  If no path is given, we use
        ctypes.util.find_library() to try to find one; if that fails,
        a CURLError is raised.
        """
        if path is None:
            path = ctypes.util.find_library('curl')
        if path is None:
            raise CURLError("libcurl not found")

        cls.libcurl_path = path
        cls.libcurl_dll = ch = ctypes.CDLL(path)

        for fname, settypes in func_type_map.items():
            try:
                fhandle = getattr(ch, fname)
            except AttributeError:
                continue  # skip this function

            pname = '_p_' + fname
            setattr(cls, pname, settypes(fhandle))

        res = ch.curl_global_init(constants.CURL_GLOBAL_ALL)
        if res != constants.CURLE_OK:
            raise CURLError("curl_global_init failed: %s" % res)

        def cleanup_libcurl():
            ch.curl_global_cleanup()

        atexit.register(cleanup_libcurl)

    def __init__(self, path=LIBCURL_LIBRARY_PATH):
        if self.libcurl_dll is None:
            type(self).load_library(path)

        self._curl = self._p_curl_easy_init()
        if self._curl is None:
            raise CURLError("curl_easy_init failed")

        # Cache of callback handles currently known to be set, so they
        # are not scooped by the GC.
        self._cbmap = {}

        # Cache of string values currently known to be set, so they
        # are not scooped by the GC.
        self._stmap = {}

    def __del__(self):
        ch = getattr(self, "libcurl_dll", None)
        cs = getattr(self, "_curl", None)
        if None not in (ch, cs):
            ch.curl_easy_cleanup(cs)

    # --- Private helper functions -------------------------------------

    def curl_call(self, fn, *args, **kw):
        """[private] Call a libcurl function and check its return
        type; throws an exception if the return value is not CURLE_OK.

        Throws CURLVersionError if the version of libcurl we are using
        does not support the requested operation, otherwise CURLError.
        """
        res = fn(self._curl, *args, **kw)
        if res != constants.CURLE_OK:
            if res == constants.CURLE_FAILED_INIT:
                raise CURLVersionError(fn.__name__, res)

            elif (fn is self._p_curl_easy_getinfo and
                  res == constants.CURLE_BAD_FUNCTION_ARGUMENT):
                raise CURLVersionError(fn.__name__, res, args[0])

            else:
                desc = self._p_curl_easy_strerror(res)
                raise CURLError('%s: %s (%s)' % (fn.__name__, desc, res), res)
        else:
            return res

    def __unpack_slist(self, ptr):
        """[private] Unpack a curl_slist into a list of strings.  Does not
        modify the list.
        """
        out = []
        cur = ptr
        while ctypes.cast(cur, ctypes.c_void_p).value is not None:
            out.append(self.DEC(cur.contents.data))
            cur = cur.contents.next

        return out

    def __setopt_bool(self, code, value):
        """[private] Set an option value that is Boolean.
        """
        v = int(bool(value))
        self.curl_call(self._p_curl_easy_setopt, code, v)

    def __setopt_int(self, code, value):
        """[private] Set an option value that is integral.  Raises
        TypeError if a value other than an int or long is passed.
        """
        if isinstance(value, int):
            self.curl_call(self._p_curl_easy_setopt, code, value)
        else:
            raise TypeError("incorrect value type", value)

    def __setopt_cstring(self, code, value):
        """[private] Set an option value that is a NUL-terminated
        string.  Accepts both string and unicode arguments, but
        unicode is encoded as UTF-8.  Raises ValueError if the encoded
        value contains a NUL byte.  Pass None to set the option to NULL.
        """
        if value is None:
            self.curl_call(self._p_curl_easy_setopt, code, curl_null)
            self._stmap.pop(code, None)
            return

        elif isinstance(value, (str, bytes, unicode)):
            v = self.ENC(value)
            if b'\0' in v:
                raise ValueError("value contains an imbedded NUL", v)

            w = ctypes.create_string_buffer(v)
            self.curl_call(self._p_curl_easy_setopt, code,
                           ctypes.cast(w, ctypes.c_void_p).value)
            self._stmap[code] = w
        else:
            raise TypeError("incorrect value type", value)

    def __setopt_strlist(self, code, values):
        """[private] Set an option value that is a linked list of
        NUL-terminated strings.  Accepts both string and unicode
        arguments, but unicode is encoded as UTF-8.  Raises ValueError
        if any encoded value contains a NUL byte.
        """
        vs = list(self.ENC(s) for s in values)
        for v in vs:
            if b'\0' in v:
                raise ValueError("value contains an imbedded NUL", v)

        lst = None
        for v in vs:
            lst = ctypes.cast(
                self._p_curl_slist_append(lst, v), ctypes.POINTER(curl_slist))

        v = curl_null if lst is None else ctypes.cast(lst,
                                                      ctypes.c_void_p).value
        self.curl_call(self._p_curl_easy_setopt, code, v)
        self._stmap[code] = vs

    def __check_func(self, value, key):
        """[private] Helper for type-checking filehandle/function values.
        """
        if hasattr(value, key):
            return getattr(value, key)
        elif value is None or hasattr(value, '__call__'):
            return value
        else:
            raise TypeError("value must have '%s' or be a function" % key,
                            value)

    def __setopt_readfunc(self, code, value):
        """[private] Set an option value expecting a function from
        which data can be read by libcurl.  The value can be either a
        filehandle, or a function taking a count and returning a string.
        """
        func = self.__check_func(value, 'read')
        if func is None:
            self.curl_call(self._p_curl_easy_setopt, code, curl_null)
            self._cbmap.pop(code, None)
            return

        def callback(buf, size, count, info_ignored):
            exp = size * count
            try:
                data = func(exp)
            except:
                return constants.CURL_READFUNC_ABORT

            act = min(exp, len(data))
            ctypes.memmove(buf, data, act)
            return act

        v = curl_readfunc_t(callback)
        self.curl_call(self._p_curl_easy_setopt, code,
                       ctypes.cast(v, ctypes.c_void_p).value)
        self._cbmap[code] = v

    def __setopt_writefunc(self, code, value):
        """[private] Set an option value expecting a function to which
        data can be written by libcurl.  The value can be either a
        filehandle, or a function taking a string to write.
        """
        func = self.__check_func(value, 'write')
        if func is None:
            self.curl_call(self._p_curl_easy_setopt, code, curl_null)
            self._cbmap.pop(code, None)
            return

        def callback(buf, size, count, info_ignored):
            data = ctypes.string_at(buf, size * count)
            try:
                res = func(data)
            except:
                return 0

            return len(data)

        v = curl_writefunc_t(callback)
        self.curl_call(self._p_curl_easy_setopt, code,
                       ctypes.cast(v, ctypes.c_void_p).value)
        self._cbmap[code] = v

    def __getinfo_wrapper(self, code, result):
        """[private] Dispatch wrapper for calls to curl_easy_getinfo().
        """
        self.curl_call(self._p_curl_easy_getinfo, code, ctypes.byref(result))
        return result

    def __getinfo_double(self, code):
        """[private] Get an info value that returns a double.
        """
        return self.__getinfo_wrapper(code, ctypes.c_double()).value

    def __getinfo_int(self, code):
        """[private] Get an info value that returns an integer.
        """
        return self.__getinfo_wrapper(code, ctypes.c_long()).value

    def __getinfo_cstring(self, code):
        """[private] Get an info value that returns a zero-terminated string.
        Returns None if the resulting pointer is NULL.
        """
        ptr = self.__getinfo_wrapper(code, ctypes.c_char_p())
        if ptr.value is None:
            return None
        else:
            return self.DEC(ctypes.string_at(ptr))

    def __getinfo_strlist(self, code):
        """[private] Get an info value that returns a list of
        zero-terminated strings.
        """
        ptr = self.__getinfo_wrapper(code, ctypes.POINTER(curl_slist)())
        out = self.__unpack_slist(ptr)
        self._p_curl_slist_free_all(ptr)
        return out

    opt_handler = dict(
        bool=__setopt_bool,
        int=__setopt_int,
        cstring=__setopt_cstring,
        strlist=__setopt_strlist,
        readfn=__setopt_readfunc,
        writefn=__setopt_writefunc,
    )
    info_handler = dict(
        double=__getinfo_double,
        int=__getinfo_int,
        cstring=__getinfo_cstring,
        strlist=__getinfo_strlist,
    )


class Curl(CurlBase):
    """High-level interface to libcurl.
    """

    def version(self):
        """Returns a dictionary giving the versions of libcurl and its
        associated libraries currently in use.
        """
        raw = self.DEC(self._p_curl_version())
        return dict(v.split('/', 1) for v in raw.split())

    def version_info(self):
        """Returns a dictionary of the data returned by curl_version_info().
        """
        info = ctypes.cast(
            self._p_curl_version_info(constants.CURLVERSION_NOW),
            ctypes.POINTER(curl_version_info_data))

        # Extract all the simple fields, that have no complications
        out = dict(
            (key, self.DEC(getattr(info.contents, key)))
            for key in ('age', 'version', 'host', 'ssl_version',
                        'ssl_version_num', 'libz_version', 'ares', 'ares_num',
                        'libidn', 'iconv_ver_num', 'libssh_version'))

        # Unpack the 24-bit version number into a tuple
        vers = int(info.contents.version_num)
        out['version_num'] = ((vers >> 16) & 0xff, (vers >> 8) & 0xff,
                              (vers >> 0) & 0xff)

        # Unpack the feature keys in symbolic form
        out['features'] = feat = {}
        for key in ('IPV6', 'KERBEROS4', 'SSL', 'LIBZ', 'NTLM', 'GSSNEGOTIATE',
                    'DEBUG', 'CURLDEBUG', 'ASYNCHDNS', 'SPNEGO', 'LARGEFILE',
                    'IDN', 'SSPI', 'CONV'):
            real_key = 'CURL_VERSION_%s' % key
            feat[key] = bool(
                info.contents.features & getattr(constants, real_key))

        # Unpack the supported protocols into a list
        out['protocols'] = proto = []
        pos = 0
        while info.contents.protocols[pos] is not None:
            proto.append(self.DEC(info.contents.protocols[pos]))
            pos += 1

        return out

    def setopt(self, code, value):
        """Set an option value on the CURL object.
        """
        otype = options.option_type_map.get(code)
        do_setopt = self.opt_handler.get(otype)

        if do_setopt:
            do_setopt(self, code, value)
        elif otype is None:
            raise CURLError("unknown option selector", code)

        # Handle custom cases here

        else:
            raise CURLError("option selector not supported", code)

    def getinfo(self, code):
        """Get information about the current state of the CURL object.
        """
        itype = options.getinfo_type_map.get(code)
        do_getinfo = self.info_handler.get(itype)

        if do_getinfo:
            return do_getinfo(self, code)
        elif itype is None:
            raise CURLError("unknown info selector", code)

        # Handle custom cases here

        else:
            raise CURLError("info selector not supported", code)

    def perform(self):
        """Perform whatever action has been configured for the session
        handle by previous calls to .setopt().
        """
        return self.curl_call(self._p_curl_easy_perform)

    def reset(self):
        """Reset all the options of the session handle to their defaults.
        """
        self._p_curl_easy_reset(self._curl)
        self._cbmap.clear()
        self._stmap.clear()


# Here there be dragons
