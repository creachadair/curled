##
## Name:     options.py
## Purpose:  Type codes for libcurl option selectors.
##
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##
from __future__ import absolute_import

from . import constants as con

# This dictionary maps info selectors to indicators of the expected
# type for the result value.  Selectors that are not listed here must
# be handled as special cases.
#
# Codes:
#   'double'  -- a double-precision value.
#   'int'     -- an integer value
#   'cstring' -- a zero-terminated C string.
#   'strlist' -- a list of zero-terminated C strings.
#
getinfo_type_map = {
    con.CURLINFO_EFFECTIVE_URL: 'cstring',
    con.CURLINFO_RESPONSE_CODE: 'int',
    con.CURLINFO_HTTP_CONNECTCODE: 'int',
    con.CURLINFO_FILETIME: 'int',  # seconds since Unix epoch
    con.CURLINFO_TOTAL_TIME: 'double',  # seconds
    con.CURLINFO_NAMELOOKUP_TIME: 'double',  # seconds
    con.CURLINFO_CONNECT_TIME: 'double',  # seconds
    con.CURLINFO_APPCONNECT_TIME: 'double',  # seconds
    con.CURLINFO_PRETRANSFER_TIME: 'double',  # seconds
    con.CURLINFO_STARTTRANSFER_TIME: 'double',  # seconds
    con.CURLINFO_REDIRECT_TIME: 'double',  # seconds
    con.CURLINFO_REDIRECT_COUNT: 'int',
    con.CURLINFO_REDIRECT_URL: 'cstring',
    con.CURLINFO_SIZE_UPLOAD: 'double',  # bytes
    con.CURLINFO_SIZE_DOWNLOAD: 'double',  # bytes
    con.CURLINFO_SPEED_DOWNLOAD: 'double',  # bytes/second
    con.CURLINFO_SPEED_UPLOAD: 'double',  # bytes/second
    con.CURLINFO_HEADER_SIZE: 'int',  # bytes
    con.CURLINFO_REQUEST_SIZE: 'int',  # bytes
    con.CURLINFO_SSL_VERIFYRESULT: 'int',
    con.CURLINFO_SSL_ENGINES: 'strlist',
    con.CURLINFO_CONTENT_LENGTH_DOWNLOAD: 'int',
    con.CURLINFO_CONTENT_LENGTH_UPLOAD: 'int',
    con.CURLINFO_CONTENT_TYPE: 'cstring',
    con.CURLINFO_HTTPAUTH_AVAIL: 'int',  # bitmask
    con.CURLINFO_PROXYAUTH_AVAIL: 'int',  # bitmask
    con.CURLINFO_OS_ERRNO: 'int',
    con.CURLINFO_NUM_CONNECTS: 'int',
    con.CURLINFO_PRIMARY_IP: 'cstring',
    con.CURLINFO_COOKIELIST: 'strlist',
    con.CURLINFO_LASTSOCKET: 'int',
    con.CURLINFO_FTP_ENTRY_PATH: 'cstring',  # or None for NULL
    con.CURLINFO_CONDITION_UNMET: 'int',
}

# This dictionary maps option codes to indicators of the expected type
# for the option value.  Options that are not listed here must be
# handled as special cases.
#
# Codes:
#   'bool'    -- a Boolean option, converts to integer.
#   'int'     -- an integer value.
#   'cstring' -- a zero-terminated C string.
#   'strlist' -- a sequence of zero-terminated C strings.
#   'readfn'  -- a callback from which libcurl may read data.
#   'writefn' -- a callback to which libcurl may write data.
#
option_type_map = {
    # Behavior options
    con.CURLOPT_VERBOSE: 'bool',
    con.CURLOPT_HEADER: 'bool',
    con.CURLOPT_NOPROGRESS: 'bool',
    con.CURLOPT_NOSIGNAL: 'bool',

    # Callback options
    con.CURLOPT_WRITEFUNCTION: 'writefn',
    con.CURLOPT_READFUNCTION: 'readfn',
    con.CURLOPT_HEADERFUNCTION: 'writefn',

    # Error options
    con.CURLOPT_FAILONERROR: 'bool',

    # Network options
    con.CURLOPT_URL: 'cstring',
    con.CURLOPT_PROTOCOLS: 'int',  # mask of CURLPROTO_*
    con.CURLOPT_REDIR_PROTOCOLS: 'int',  # mask of CURLPROTO_*
    con.CURLOPT_PROXY: 'cstring',
    con.CURLOPT_PROXYPORT: 'int',
    con.CURLOPT_PROXYTYPE: 'int',  # value in CURLPROXY_*
    con.CURLOPT_NOPROXY: 'cstring',
    con.CURLOPT_HTTPPROXYTUNNEL: 'bool',
    con.CURLOPT_SOCKS5_GSSAPI_SERVICE: 'cstring',
    con.CURLOPT_SOCKS5_GSSAPI_NEC: 'bool',
    con.CURLOPT_INTERFACE: 'cstring',
    con.CURLOPT_LOCALPORT: 'int',
    con.CURLOPT_LOCALPORTRANGE: 'int',
    con.CURLOPT_DNS_CACHE_TIMEOUT: 'int',
    con.CURLOPT_DNS_USE_GLOBAL_CACHE: 'bool',
    con.CURLOPT_BUFFERSIZE: 'int',
    con.CURLOPT_PORT: 'int',
    con.CURLOPT_TCP_NODELAY: 'bool',
    con.CURLOPT_ADDRESS_SCOPE: 'int',

    # Names and Passwords options
    con.CURLOPT_NETRC: 'int',  # value in CURL_NETRC_*
    con.CURLOPT_NETRC_FILE: 'cstring',
    con.CURLOPT_USERPWD: 'cstring',
    con.CURLOPT_PROXYUSERPWD: 'cstring',
    con.CURLOPT_USERNAME: 'cstring',
    con.CURLOPT_PASSWORD: 'cstring',
    con.CURLOPT_PROXYUSERNAME: 'cstring',
    con.CURLOPT_PROXYPASSWORD: 'cstring',
    con.CURLOPT_HTTPAUTH: 'int',  # mask of CURLAUTH_*
    con.CURLOPT_PROXYAUTH: 'int',  # mask of CURLAUTH_*

    # HTTP options
    con.CURLOPT_AUTOREFERER: 'bool',
    con.CURLOPT_ENCODING: 'cstring',
    con.CURLOPT_FOLLOWLOCATION: 'bool',
    con.CURLOPT_UNRESTRICTED_AUTH: 'bool',
    con.CURLOPT_MAXREDIRS: 'int',
    con.CURLOPT_POSTREDIR: 'int',  # mask of CURL_REDIR_*
    con.CURLOPT_POST: 'bool',
    con.CURLOPT_POSTFIELDSIZE: 'int',
    con.CURLOPT_REFERER: 'cstring',
    con.CURLOPT_USERAGENT: 'cstring',
    con.CURLOPT_HTTPHEADER: 'strlist',
    con.CURLOPT_HTTP200ALIASES: 'strlist',
    con.CURLOPT_COOKIE: 'cstring',
    con.CURLOPT_COOKIEFILE: 'cstring',
    con.CURLOPT_COOKIEJAR: 'cstring',
    con.CURLOPT_COOKIESESSION: 'bool',
    con.CURLOPT_COOKIELIST: 'cstring',
    con.CURLOPT_HTTPGET: 'bool',
    con.CURLOPT_HTTP_VERSION: 'int',  # value in CURL_HTTP_VERSION_*
    con.CURLOPT_IGNORE_CONTENT_LENGTH: 'bool',
    con.CURLOPT_HTTP_CONTENT_DECODING: 'bool',
    con.CURLOPT_HTTP_TRANSFER_DECODING: 'bool',

    # TFTP options
    con.CURLOPT_TFTP_BLKSIZE: 'int',  # 8 <= v <= 65464, per RFC 2348

    # FTP options
    con.CURLOPT_FTPPORT: 'cstring',
    con.CURLOPT_QUOTE: 'strlist',
    con.CURLOPT_POSTQUOTE: 'strlist',
    con.CURLOPT_PREQUOTE: 'strlist',
    con.CURLOPT_DIRLISTONLY: 'bool',
    con.CURLOPT_APPEND: 'bool',
    con.CURLOPT_FTP_USE_EPRT: 'bool',
    con.CURLOPT_FTP_USE_EPSV: 'bool',
    con.CURLOPT_FTP_CREATE_MISSING_DIRS: 'int',  # value in CURLFTP_CREATE_DIR_*
    con.CURLOPT_FTP_RESPONSE_TIMEOUT: 'int',  # seconds
    con.CURLOPT_FTP_ALTERNATIVE_TO_USER: 'cstring',
    con.CURLOPT_FTP_SKIP_PASV_IP: 'bool',
    con.CURLOPT_USE_SSL: 'int',  # value in CURLUSESSL_*
    con.CURLOPT_FTPSSLAUTH: 'int',  # value in CURLFTPAUTH_*
    con.CURLOPT_FTP_SSL_CCC: 'int',  # value in CURLFTPSSL_CCC_*
    con.CURLOPT_FTP_ACCOUNT: 'cstring',
    con.CURLOPT_FTP_FILEMETHOD: 'int',  # value in CURLFTPMETHOD_*

    # Protocol options
    con.CURLOPT_TRANSFERTEXT: 'bool',
    con.CURLOPT_PROXY_TRANSFER_MODE: 'bool',
    con.CURLOPT_CRLF: 'bool',
    con.CURLOPT_RANGE: 'cstring',
    con.CURLOPT_RESUME_FROM: 'int',
    con.CURLOPT_CUSTOMREQUEST: 'cstring',
    con.CURLOPT_FILETIME: 'bool',
    con.CURLOPT_NOBODY: 'bool',
    con.CURLOPT_INFILESIZE: 'int',
    con.CURLOPT_INFILESIZE_LARGE: 'int',
    con.CURLOPT_UPLOAD: 'bool',
    con.CURLOPT_MAXFILESIZE: 'int',
    con.CURLOPT_TIMECONDITION: 'int',  # value in CURL_TIMECOND_*
    con.CURLOPT_TIMEVALUE: 'int',  # seconds since Unix epoch

    # Connection options
    con.CURLOPT_TIMEOUT: 'int',  # seconds
    con.CURLOPT_TIMEOUT_MS: 'int',  # milliseconds
    con.CURLOPT_LOW_SPEED_LIMIT: 'int',  # bytes/sec.
    con.CURLOPT_LOW_SPEED_TIME: 'int',  # seconds
    con.CURLOPT_MAXCONNECTS: 'int',
    con.CURLOPT_FRESH_CONNECT: 'bool',
    con.CURLOPT_FORBID_REUSE: 'bool',
    con.CURLOPT_CONNECTTIMEOUT: 'int',  # seconds
    con.CURLOPT_CONNECTTIMEOUT_MS: 'int',  # milliseconds
    con.CURLOPT_IPRESOLVE: 'int',  # value in CURL_IPRESOLVE_*
    con.CURLOPT_CONNECT_ONLY: 'bool',

    # SSL and Security options
    con.CURLOPT_SSLCERT: 'cstring',
    con.CURLOPT_SSLCERTTYPE: 'cstring',
    con.CURLOPT_SSLKEY: 'cstring',
    con.CURLOPT_SSLKEYTYPE: 'cstring',
    con.CURLOPT_KEYPASSWD: 'cstring',
    con.CURLOPT_SSLENGINE: 'cstring',
    con.CURLOPT_SSLVERSION: 'int',  # value in CURL_SSLVERSION_*
    con.CURLOPT_SSL_VERIFYPEER: 'bool',
    con.CURLOPT_CAINFO: 'cstring',
    con.CURLOPT_ISSUERCERT: 'cstring',
    con.CURLOPT_CAPATH: 'cstring',
    con.CURLOPT_CRLFILE: 'cstring',
    con.CURLOPT_CERTINFO: 'bool',
    con.CURLOPT_RANDOM_FILE: 'cstring',
    con.CURLOPT_EGDSOCKET: 'cstring',
    con.CURLOPT_SSL_VERIFYHOST: 'int',
    con.CURLOPT_SSL_CIPHER_LIST: 'cstring',
    con.CURLOPT_SSL_SESSIONID_CACHE: 'bool',
    con.CURLOPT_KRBLEVEL: 'cstring',

    # SSH options
    con.CURLOPT_SSH_AUTH_TYPES: 'int',  # mask of CURLAUTH_SSH_*
    con.CURLOPT_SSH_PUBLIC_KEYFILE: 'cstring',
    con.CURLOPT_SSH_PRIVATE_KEYFILE: 'cstring',
    con.CURLOPT_SSH_KNOWNHOSTS: 'cstring',
    con.CURLOPT_SSH_HOST_PUBLIC_KEY_MD5: 'cstring',

    # Other options
    con.CURLOPT_NEW_FILE_PERMS: 'int',  # POSIX permission word
    con.CURLOPT_NEW_DIRECTORY_PERMS: 'int',  # POSIX permission word

    # Telnet options
    con.CURLOPT_TELNETOPTIONS: 'strlist',
}

__all__ = ('option_type_map',)

# Here there be dragons
