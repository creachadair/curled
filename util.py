##
## Name:     util.py
## Purpose:  Helpful functions for using libcurl.
##
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##
from __future__ import absolute_import

import io
from . import objects, constants


class url_result(object):
    """A file-like object representing the results of a cURL query.

    Attributes:
    .url        -- the original URL requested.
    .actual_url -- the actual URL loaded, after redirection.
    .headers    -- a list of (name, value) tuples for HTTP headers.
    .code       -- the response code from the server.
    .duration   -- how long the request took, in seconds (float).
    """

    def __init__(self, url):
        self.url = url
        self.actual_url = url
        self.headers = []
        self.code = None
        self.duration = None
        self.data = io.BytesIO()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.data.close()

    def read(self, *nc):
        return self.data.read(*nc)

    def readline(self):
        return self.data.readline()

    def seek(self, pos, *rel):
        self.data.seek(pos, *rel)

    def tell(self):
        return self.data.tell()

    def length(self):
        SEEK_END = 2
        save = self.data.tell()
        try:
            self.data.seek(0, SEEK_END)
            return self.data.tell()
        finally:
            self.data.seek(save)

    def keys(self):
        return list(set(s for s, t in self.headers))

    def close(self):
        return self.data.close()

    def __getitem__(self, itm):
        for s, t in self.headers:
            if itm.lower() == s.lower():
                return t
        else:
            raise KeyError(itm)


def fetch_url(url, headers={}, curl_obj=None):
    """Download the specified URL and return a file-like object to
    represent it.  The headers, if specified, are included with the
    request to the server.

    If no Curl object is specified, a new one will be created for each
    request.  To specify custom settings, create your own and pass it
    via the curl_obj parameter.  Note that some of the options of your
    object will be modified when this occurs.

    This function is similar in spirit to urllib.urlopen().
    """
    if curl_obj is None:
        c = objects.Curl()
        c.setopt(constants.CURLOPT_FOLLOWLOCATION, True)
        c.setopt(constants.CURLOPT_MAXREDIRS, 5)
    else:
        c = curl_obj

    u = url_result(url)
    c.setopt(constants.CURLOPT_URL, url)
    c.setopt(constants.CURLOPT_WRITEFUNCTION, u.data)

    def recv_header(buf):
        if b':' in buf:
            key, val = buf.rstrip(b'\r\n').split(b':', 1)
            u.headers.append((key, val.lstrip()))

    c.setopt(constants.CURLOPT_HEADERFUNCTION, recv_header)
    if headers:
        c.setopt(constants.CURLOPT_HTTPHEADER,
                 list('%s: %s' % (k, v) for k, v in headers.items()))
    c.perform()

    u.actual_url = c.getinfo(constants.CURLINFO_EFFECTIVE_URL)
    u.duration = c.getinfo(constants.CURLINFO_TOTAL_TIME)
    u.code = c.getinfo(constants.CURLINFO_RESPONSE_CODE)

    u.seek(0)
    return u


def track_location(url, headers={}):
    """Return a list of the URL's, beginning from the one given,
    that will be traversed when following the redirect chain from
    the starting URL.
    """
    c = objects.Curl()
    c.setopt(constants.CURLOPT_FOLLOWLOCATION, False)
    c.setopt(constants.CURLOPT_NOBODY, True)

    cur = url
    out = [url]
    while True:
        u = fetch_url(cur, headers, c)
        v = c.getinfo(constants.CURLINFO_REDIRECT_URL)
        if v is None or v in out:
            break
        out.append(v)
        cur = v

    return out


__all__ = ('fetch_url', 'track_location')

# Here there be dragons
