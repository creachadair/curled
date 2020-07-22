#!/usr/bin/env python
##
## Name:     make_const.py
## Purpose:  Make the "constants" module.
##
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##

import errno, os, sys

SECTION_COMMENT = {
    'CURLcode': 'Return codes from curl_easy_* functions',
    'CURLFORMcode': 'Return codes for curl_formadd()',
    'CURLSHcode': 'Return codes for curl_share_stopt()',
    'CURLSHoption': 'Option codes for curl_share_setopt()',
    'CURLformoption': 'Option codes for CURLFORM_ARRAY values',
    'CURLoption': 'Option codes for curl_easy_setopt()',
    'CURLversion': 'Version selectors for curl_version_info()',
    'curlversioncodes': 'Bit masks for curl_version_info_data->features',
    'curl_TimeCond': 'Option codes for CURLOPT_TIMECONDITION',
    'curl_closepolicy': 'Option codes for CURLOPT_CLOSEPOLICY',
    'curl_ftpauth': 'Option codes for CURLOPT_FTPSSLAUTH',
    'curl_ftpccc': 'Option codes for CURLOPT_FTP_SSL_CCC',
    'curl_ftpcreatedir': 'Option codes for CURLOPT_FTP_CREATE_MISSING_DIRS',
    'curl_ftpmethod': 'Option codes for CURLOPT_FTP_FILEMETHOD',
    'curl_infotype':
    'Specifies the kind of data passed to information_callback',
    'curl_lock_access': 'Specifies lock access type for lock functions',
    'curl_lock_data': 'Different data locks for a single share',
    'curl_proxytype': 'Option codes for CURLOPT_PROXYTYPE',
    'curl_usessl': 'Option codes for CURLOPT_USE_SSL',
    'curlauth': 'Option codes for CURLOPT_HTTPAUTH',
    'curlglobal': 'Flags for curl_global_init()',
    'CURLINFO': 'Selector codes for curl_easy_getinfo()',
    'curliocmd': 'Operation codes for ioctl callbacks',
    'curlioerr': 'Return codes for ioctl callbacks',
    'curlopttype': 'Option type codes',
    'curlpause': 'Bit masks for curl_easy_pause()',
    'curlproto':
    'Option bitmasks for CURLOPT_PROTOCOLS and CURLOPT_REDIR_PROTOCOLS',
    'curlsshauth': 'Option bitmasks for CURLOPT_SSH_AUTH_TYPES',
    'curlsocktype': 'Socket type selector for sockopt callback',
    'httpversion': 'Option codes for CURLOPT_HTTP_VERSION',
    'ipresolve': 'Option codes for CURLOPT_IPRESOLVE',
    'netrcoption': 'Option codes for CURLOPT_NETRC',
    'redirflags': 'Option codes for CURLOPT_POSTREDIR',
    'sslversion': 'Option codes for CURLOPT_SSLVERSION',
}


def format_section_comment(com):
    base = '# --- %s ' % com
    if len(base) < 72:
        base += '-' * (72 - len(base))

    return base


def extract_defines(include_dirs=()):
    if not os.path.isfile("curlextract.c"):
        raise KeyError("curlextract.c is missing")
    if os.path.exists("curlextract"):
        os.unlink("curlextract")

    args = ['gcc', '-o', 'curlextract']
    for v in include_dirs:
        args.append('-I')
        args.append(v)
    args.append("curlextract.c")

    res = os.spawnvp(os.P_WAIT, args[0], args)
    if res != 0:
        raise ValueError("compilation error: %s" % res)

    result = {None: []}
    curid = None
    with os.popen('./curlextract', 'r') as cmd:
        for line in cmd:
            if line.startswith('@'):
                curid = line[1:].rstrip()
            else:
                key, val = line.rstrip().split('=', 1)
                result.setdefault(curid, []).append((key, val))

    if not result[None]:
        result.pop(None)

    os.unlink("curlextract")
    return result


def write_module(defs, ofp):
    ofp.write('''
##
## Name:     constants.py
## Purpose:  Symbolic constants used by libcurl.
##
## Copyright (c) Michael J. Fromberger, All Rights Reserved.
##
## This file was mechanically generated by extracting the names
## defined in <curl/curl.h>
##
##\n'''.lstrip())

    name_width = max(max(len(k) for k, v in d) for d in defs.values())
    val_template = '%%(key)-%ds = %%(value)s\n' % name_width

    for sect in sorted(defs.keys(), key=lambda s: s.lower()):
        com = SECTION_COMMENT.get(sect)

        ofp.write('\n')
        if com is not None:
            ofp.write(format_section_comment(com))
            ofp.write('\n')

        for key, val in defs[sect]:
            ofp.write(val_template % {'key': key, 'value': val})

    ofp.write('\n# Here there be dragons\n')


def main(argv):
    defs = extract_defines(['/opt/local/include'])
    with file('constants.py', 'wt') as fp:
        write_module(defs, fp)

    return 0


if __name__ == '__main__':
    res = main(sys.argv[1:])
    sys.exit(res)

# Here there be dragons
