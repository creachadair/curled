/*
  Name:     curlextract.c
  Purpose:  Extract symbolic constants from the cURL headers.

  Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.

  This program basically just converts the symbolic constants from the curl.h
  header into a format that can be processed by a Python program.  The compiler
  does all the work; this is just a wrapper to convert the results to text.
 */

#include <errno.h>
#include <stdio.h>
#include <string.h>

#include <curl/curl.h>

#define X(name) printf(#name "=%d\n", name)

int main(int argc, char *argv[]) {
  printf("@CURLcode\n");
  X(CURLE_OK);
  X(CURLE_UNSUPPORTED_PROTOCOL);
  X(CURLE_FAILED_INIT);
  X(CURLE_URL_MALFORMAT);
  X(CURLE_COULDNT_RESOLVE_PROXY);
  X(CURLE_COULDNT_RESOLVE_HOST);
  X(CURLE_COULDNT_CONNECT);
  X(CURLE_FTP_WEIRD_SERVER_REPLY);
  X(CURLE_REMOTE_ACCESS_DENIED);
  X(CURLE_FTP_WEIRD_PASS_REPLY);
  X(CURLE_FTP_WEIRD_PASV_REPLY);
  X(CURLE_FTP_WEIRD_227_FORMAT);
  X(CURLE_FTP_CANT_GET_HOST);
  X(CURLE_FTP_COULDNT_SET_TYPE);
  X(CURLE_PARTIAL_FILE);
  X(CURLE_FTP_COULDNT_RETR_FILE);
  X(CURLE_QUOTE_ERROR);
  X(CURLE_HTTP_RETURNED_ERROR);
  X(CURLE_WRITE_ERROR);
  X(CURLE_UPLOAD_FAILED);
  X(CURLE_READ_ERROR);
  X(CURLE_OUT_OF_MEMORY);
  X(CURLE_OPERATION_TIMEDOUT);
  X(CURLE_FTP_PORT_FAILED);
  X(CURLE_FTP_COULDNT_USE_REST);
  X(CURLE_RANGE_ERROR);
  X(CURLE_HTTP_POST_ERROR);
  X(CURLE_SSL_CONNECT_ERROR);
  X(CURLE_BAD_DOWNLOAD_RESUME);
  X(CURLE_FILE_COULDNT_READ_FILE);
  X(CURLE_LDAP_CANNOT_BIND);
  X(CURLE_LDAP_SEARCH_FAILED);
  X(CURLE_FUNCTION_NOT_FOUND);
  X(CURLE_ABORTED_BY_CALLBACK);
  X(CURLE_BAD_FUNCTION_ARGUMENT);
  X(CURLE_INTERFACE_FAILED);
  X(CURLE_TOO_MANY_REDIRECTS);
  X(CURLE_UNKNOWN_TELNET_OPTION);
  X(CURLE_TELNET_OPTION_SYNTAX);
  X(CURLE_PEER_FAILED_VERIFICATION);
  X(CURLE_GOT_NOTHING);
  X(CURLE_SSL_ENGINE_NOTFOUND);
  X(CURLE_SSL_ENGINE_SETFAILED);
  X(CURLE_SEND_ERROR);
  X(CURLE_RECV_ERROR);
  X(CURLE_SSL_CERTPROBLEM);
  X(CURLE_SSL_CIPHER);
  X(CURLE_SSL_CACERT);
  X(CURLE_BAD_CONTENT_ENCODING);
  X(CURLE_LDAP_INVALID_URL);
  X(CURLE_FILESIZE_EXCEEDED);
  X(CURLE_USE_SSL_FAILED);
  X(CURLE_SEND_FAIL_REWIND);
  X(CURLE_SSL_ENGINE_INITFAILED);
  X(CURLE_LOGIN_DENIED);
  X(CURLE_TFTP_NOTFOUND);
  X(CURLE_TFTP_PERM);
  X(CURLE_REMOTE_DISK_FULL);
  X(CURLE_TFTP_ILLEGAL);
  X(CURLE_TFTP_UNKNOWNID);
  X(CURLE_REMOTE_FILE_EXISTS);
  X(CURLE_TFTP_NOSUCHUSER);
  X(CURLE_CONV_FAILED);
  X(CURLE_CONV_REQD);
  X(CURLE_SSL_CACERT_BADFILE);
  X(CURLE_REMOTE_FILE_NOT_FOUND);
  X(CURLE_SSH);
  X(CURLE_SSL_SHUTDOWN_FAILED);
  X(CURLE_AGAIN);
  X(CURLE_SSL_CRL_BADFILE);
  X(CURLE_SSL_ISSUER_ERROR);

  printf("@CURLFORMcode\n");
  X(CURL_FORMADD_OK);
  X(CURL_FORMADD_MEMORY);
  X(CURL_FORMADD_OPTION_TWICE);
  X(CURL_FORMADD_NULL);
  X(CURL_FORMADD_UNKNOWN_OPTION);
  X(CURL_FORMADD_INCOMPLETE);
  X(CURL_FORMADD_ILLEGAL_ARRAY);
  X(CURL_FORMADD_DISABLED);

  printf("@CURLSHcode\n");
  X(CURLSHE_OK);
  X(CURLSHE_BAD_OPTION);
  X(CURLSHE_IN_USE);
  X(CURLSHE_INVALID);
  X(CURLSHE_NOMEM);

  printf("@CURLSHoption\n");
  X(CURLSHOPT_SHARE);
  X(CURLSHOPT_UNSHARE);
  X(CURLSHOPT_LOCKFUNC);
  X(CURLSHOPT_UNLOCKFUNC);
  X(CURLSHOPT_USERDATA);

  printf("@CURLformoption\n");
  X(CURLFORM_COPYNAME);
  X(CURLFORM_PTRNAME);
  X(CURLFORM_NAMELENGTH);
  X(CURLFORM_COPYCONTENTS);
  X(CURLFORM_PTRCONTENTS);
  X(CURLFORM_CONTENTSLENGTH);
  X(CURLFORM_FILECONTENT);
  X(CURLFORM_ARRAY);
  X(CURLFORM_FILE);
  X(CURLFORM_BUFFER);
  X(CURLFORM_BUFFERPTR);
  X(CURLFORM_BUFFERLENGTH);
  X(CURLFORM_CONTENTTYPE);
  X(CURLFORM_CONTENTHEADER);
  X(CURLFORM_FILENAME);
  X(CURLFORM_END);
  X(CURLFORM_STREAM);

  printf("@CURLoption\n");
  X(CURLOPT_FILE);
  X(CURLOPT_URL);
  X(CURLOPT_PORT);
  X(CURLOPT_PROXY);
  X(CURLOPT_USERPWD);
  X(CURLOPT_PROXYUSERPWD);
  X(CURLOPT_RANGE);
  X(CURLOPT_INFILE);
  X(CURLOPT_ERRORBUFFER);
  X(CURLOPT_WRITEFUNCTION);
  X(CURL_WRITEFUNC_PAUSE);
  X(CURLOPT_READFUNCTION);
  X(CURL_READFUNC_ABORT);
  X(CURL_READFUNC_PAUSE);
  X(CURLOPT_TIMEOUT);
  X(CURLOPT_INFILESIZE);
  X(CURLOPT_POSTFIELDS);
  X(CURLOPT_REFERER);
  X(CURLOPT_FTPPORT);
  X(CURLOPT_USERAGENT);
  X(CURLOPT_LOW_SPEED_LIMIT);
  X(CURLOPT_LOW_SPEED_TIME);
  X(CURLOPT_RESUME_FROM);
  X(CURLOPT_COOKIE);
  X(CURLOPT_HTTPHEADER);
  X(CURLOPT_HTTPPOST);
  X(CURLOPT_SSLCERT);
  X(CURLOPT_KEYPASSWD);
  X(CURLOPT_CRLF);
  X(CURLOPT_QUOTE);
  X(CURLOPT_WRITEHEADER);
  X(CURLOPT_COOKIEFILE);
  X(CURLOPT_SSLVERSION);
  X(CURLOPT_TIMECONDITION);
  X(CURLOPT_TIMEVALUE);
  X(CURLOPT_CUSTOMREQUEST);
  X(CURLOPT_STDERR);
  X(CURLOPT_POSTQUOTE);
  X(CURLOPT_WRITEINFO);
  X(CURLOPT_VERBOSE);
  X(CURLOPT_HEADER);
  X(CURLOPT_NOPROGRESS);
  X(CURLOPT_NOBODY);
  X(CURLOPT_FAILONERROR);
  X(CURLOPT_UPLOAD);
  X(CURLOPT_POST);
  X(CURLOPT_DIRLISTONLY);
  X(CURLOPT_APPEND);
  X(CURLOPT_NETRC);
  X(CURLOPT_FOLLOWLOCATION);
  X(CURLOPT_TRANSFERTEXT);
  X(CURLOPT_PUT);
  X(CURLOPT_PROGRESSFUNCTION);
  X(CURLOPT_PROGRESSDATA);
  X(CURLOPT_AUTOREFERER);
  X(CURLOPT_PROXYPORT);
  X(CURLOPT_POSTFIELDSIZE);
  X(CURLOPT_HTTPPROXYTUNNEL);
  X(CURLOPT_INTERFACE);
  X(CURLOPT_KRBLEVEL);
  X(CURLOPT_SSL_VERIFYPEER);
  X(CURLOPT_CAINFO);
  X(CURLOPT_MAXREDIRS);
  X(CURLOPT_FILETIME);
  X(CURLOPT_TELNETOPTIONS);
  X(CURLOPT_MAXCONNECTS);
  X(CURLOPT_CLOSEPOLICY);
  X(CURLOPT_FRESH_CONNECT);
  X(CURLOPT_FORBID_REUSE);
  X(CURLOPT_RANDOM_FILE);
  X(CURLOPT_EGDSOCKET);
  X(CURLOPT_CONNECTTIMEOUT);
  X(CURLOPT_HEADERFUNCTION);
  X(CURLOPT_HTTPGET);
  X(CURLOPT_SSL_VERIFYHOST);
  X(CURLOPT_COOKIEJAR);
  X(CURLOPT_SSL_CIPHER_LIST);
  X(CURLOPT_HTTP_VERSION);
  X(CURLOPT_FTP_USE_EPSV);
  X(CURLOPT_SSLCERTTYPE);
  X(CURLOPT_SSLKEY);
  X(CURLOPT_SSLKEYTYPE);
  X(CURLOPT_SSLENGINE);
  X(CURLOPT_SSLENGINE_DEFAULT);
  X(CURLOPT_DNS_USE_GLOBAL_CACHE);
  X(CURLOPT_DNS_CACHE_TIMEOUT);
  X(CURLOPT_PREQUOTE);
  X(CURLOPT_DEBUGFUNCTION);
  X(CURLOPT_DEBUGDATA);
  X(CURLOPT_COOKIESESSION);
  X(CURLOPT_CAPATH);
  X(CURLOPT_BUFFERSIZE);
  X(CURLOPT_NOSIGNAL);
  X(CURLOPT_SHARE);
  X(CURLOPT_PROXYTYPE);
  X(CURLOPT_ENCODING);
  X(CURLOPT_PRIVATE);
  X(CURLOPT_HTTP200ALIASES);
  X(CURLOPT_UNRESTRICTED_AUTH);
  X(CURLOPT_FTP_USE_EPRT);
  X(CURLOPT_HTTPAUTH);
  X(CURLOPT_SSL_CTX_FUNCTION);
  X(CURLOPT_SSL_CTX_DATA);
  X(CURLOPT_FTP_CREATE_MISSING_DIRS);
  X(CURLOPT_PROXYAUTH);
  X(CURLOPT_FTP_RESPONSE_TIMEOUT);
  X(CURLOPT_IPRESOLVE);
  X(CURLOPT_MAXFILESIZE);
  X(CURLOPT_INFILESIZE_LARGE);
  X(CURLOPT_RESUME_FROM_LARGE);
  X(CURLOPT_MAXFILESIZE_LARGE);
  X(CURLOPT_NETRC_FILE);
  X(CURLOPT_USE_SSL);
  X(CURLOPT_POSTFIELDSIZE_LARGE);
  X(CURLOPT_TCP_NODELAY);
  X(CURLOPT_FTPSSLAUTH);
  X(CURLOPT_IOCTLFUNCTION);
  X(CURLOPT_IOCTLDATA);
  X(CURLOPT_FTP_ACCOUNT);
  X(CURLOPT_COOKIELIST);
  X(CURLOPT_IGNORE_CONTENT_LENGTH);
  X(CURLOPT_FTP_SKIP_PASV_IP);
  X(CURLOPT_FTP_FILEMETHOD);
  X(CURLOPT_LOCALPORT);
  X(CURLOPT_LOCALPORTRANGE);
  X(CURLOPT_CONNECT_ONLY);
  X(CURLOPT_CONV_FROM_NETWORK_FUNCTION);
  X(CURLOPT_CONV_TO_NETWORK_FUNCTION);
  X(CURLOPT_CONV_FROM_UTF8_FUNCTION);
  X(CURLOPT_MAX_SEND_SPEED_LARGE);
  X(CURLOPT_MAX_RECV_SPEED_LARGE);
  X(CURLOPT_FTP_ALTERNATIVE_TO_USER);
  X(CURLOPT_SOCKOPTFUNCTION);
  X(CURLOPT_SOCKOPTDATA);
  X(CURLOPT_SSL_SESSIONID_CACHE);
  X(CURLOPT_SSH_AUTH_TYPES);
  X(CURLOPT_SSH_PUBLIC_KEYFILE);
  X(CURLOPT_SSH_PRIVATE_KEYFILE);
  X(CURLOPT_FTP_SSL_CCC);
  X(CURLOPT_TIMEOUT_MS);
  X(CURLOPT_CONNECTTIMEOUT_MS);
  X(CURLOPT_HTTP_TRANSFER_DECODING);
  X(CURLOPT_HTTP_CONTENT_DECODING);
  X(CURLOPT_NEW_FILE_PERMS);
  X(CURLOPT_NEW_DIRECTORY_PERMS);
  X(CURLOPT_POSTREDIR);
  X(CURLOPT_SSH_HOST_PUBLIC_KEY_MD5);
  X(CURLOPT_OPENSOCKETFUNCTION);
  X(CURLOPT_OPENSOCKETDATA);
  X(CURLOPT_COPYPOSTFIELDS);
  X(CURLOPT_PROXY_TRANSFER_MODE);
  X(CURLOPT_SEEKFUNCTION);
  X(CURL_SEEKFUNC_OK);
  X(CURL_SEEKFUNC_FAIL);
  X(CURL_SEEKFUNC_CANTSEEK);
  X(CURLOPT_SEEKDATA);
  X(CURLOPT_CRLFILE);
  X(CURLOPT_ISSUERCERT);
  X(CURLOPT_ADDRESS_SCOPE);
  X(CURLOPT_CERTINFO);
  X(CURLOPT_USERNAME);
  X(CURLOPT_PASSWORD);
  X(CURLOPT_PROXYUSERNAME);
  X(CURLOPT_PROXYPASSWORD);
  X(CURLOPT_NOPROXY);
  X(CURLOPT_TFTP_BLKSIZE);
  X(CURLOPT_SOCKS5_GSSAPI_SERVICE);
  X(CURLOPT_SOCKS5_GSSAPI_NEC);
  X(CURLOPT_PROTOCOLS);
  X(CURLOPT_REDIR_PROTOCOLS);
  X(CURLOPT_SSH_KNOWNHOSTS);

  printf("@CURLversion\n");
  X(CURLVERSION_FIRST);
  X(CURLVERSION_SECOND);
  X(CURLVERSION_THIRD);
  X(CURLVERSION_FOURTH);
  X(CURLVERSION_NOW);

  printf("@curl_TimeCond\n");
  X(CURL_TIMECOND_NONE);
  X(CURL_TIMECOND_IFMODSINCE);
  X(CURL_TIMECOND_IFUNMODSINCE);
  X(CURL_TIMECOND_LASTMOD);

  printf("@curl_closepolicy\n");
  X(CURLCLOSEPOLICY_OLDEST);
  X(CURLCLOSEPOLICY_LEAST_RECENTLY_USED);
  X(CURLCLOSEPOLICY_LEAST_TRAFFIC);
  X(CURLCLOSEPOLICY_SLOWEST);
  X(CURLCLOSEPOLICY_CALLBACK);

  printf("@curl_ftpauth\n");
  X(CURLFTPAUTH_DEFAULT);
  X(CURLFTPAUTH_SSL);
  X(CURLFTPAUTH_TLS);

  printf("@curl_ftpccc\n");
  X(CURLFTPSSL_CCC_NONE);
  X(CURLFTPSSL_CCC_PASSIVE);
  X(CURLFTPSSL_CCC_ACTIVE);

  printf("@curl_ftpcreatedir\n");
  X(CURLFTP_CREATE_DIR_NONE);
  X(CURLFTP_CREATE_DIR);
  X(CURLFTP_CREATE_DIR_RETRY);

  printf("@curl_ftpmethod\n");
  X(CURLFTPMETHOD_DEFAULT);
  X(CURLFTPMETHOD_MULTICWD);
  X(CURLFTPMETHOD_NOCWD);
  X(CURLFTPMETHOD_SINGLECWD);

  printf("@curl_infotype\n");
  X(CURLINFO_TEXT);
  X(CURLINFO_HEADER_IN);
  X(CURLINFO_HEADER_OUT);
  X(CURLINFO_DATA_IN);
  X(CURLINFO_DATA_OUT);
  X(CURLINFO_SSL_DATA_IN);
  X(CURLINFO_SSL_DATA_OUT);

  printf("@curl_lock_access\n");
  X(CURL_LOCK_ACCESS_NONE);
  X(CURL_LOCK_ACCESS_SHARED);
  X(CURL_LOCK_ACCESS_SINGLE);

  printf("@curl_lock_data\n");
  X(CURL_LOCK_DATA_NONE);
  X(CURL_LOCK_DATA_SHARE);
  X(CURL_LOCK_DATA_COOKIE);
  X(CURL_LOCK_DATA_DNS);
  X(CURL_LOCK_DATA_SSL_SESSION);
  X(CURL_LOCK_DATA_CONNECT);

  printf("@curl_proxytype\n");
  X(CURLPROXY_HTTP);
  X(CURLPROXY_HTTP_1_0);
  X(CURLPROXY_SOCKS4);
  X(CURLPROXY_SOCKS5);
  X(CURLPROXY_SOCKS4A);
  X(CURLPROXY_SOCKS5_HOSTNAME);

  printf("@curl_usessl\n");
  X(CURLUSESSL_NONE);
  X(CURLUSESSL_TRY);
  X(CURLUSESSL_CONTROL);
  X(CURLUSESSL_ALL);

  printf("@curlglobal\n");
  X(CURL_GLOBAL_SSL);
  X(CURL_GLOBAL_WIN32);
  X(CURL_GLOBAL_ALL);
  X(CURL_GLOBAL_NOTHING);
  X(CURL_GLOBAL_DEFAULT);

  printf("@CURLINFO\n");
  X(CURLINFO_EFFECTIVE_URL);
  X(CURLINFO_RESPONSE_CODE);
  X(CURLINFO_TOTAL_TIME);
  X(CURLINFO_NAMELOOKUP_TIME);
  X(CURLINFO_CONNECT_TIME);
  X(CURLINFO_PRETRANSFER_TIME);
  X(CURLINFO_SIZE_UPLOAD);
  X(CURLINFO_SIZE_DOWNLOAD);
  X(CURLINFO_SPEED_DOWNLOAD);
  X(CURLINFO_SPEED_UPLOAD);
  X(CURLINFO_HEADER_SIZE);
  X(CURLINFO_REQUEST_SIZE);
  X(CURLINFO_SSL_VERIFYRESULT);
  X(CURLINFO_FILETIME);
  X(CURLINFO_CONTENT_LENGTH_DOWNLOAD);
  X(CURLINFO_CONTENT_LENGTH_UPLOAD);
  X(CURLINFO_STARTTRANSFER_TIME);
  X(CURLINFO_CONTENT_TYPE);
  X(CURLINFO_REDIRECT_TIME);
  X(CURLINFO_REDIRECT_COUNT);
  X(CURLINFO_PRIVATE);
  X(CURLINFO_HTTP_CONNECTCODE);
  X(CURLINFO_HTTPAUTH_AVAIL);
  X(CURLINFO_PROXYAUTH_AVAIL);
  X(CURLINFO_OS_ERRNO);
  X(CURLINFO_NUM_CONNECTS);
  X(CURLINFO_SSL_ENGINES);
  X(CURLINFO_COOKIELIST);
  X(CURLINFO_LASTSOCKET);
  X(CURLINFO_FTP_ENTRY_PATH);
  X(CURLINFO_REDIRECT_URL);
  X(CURLINFO_PRIMARY_IP);
  X(CURLINFO_APPCONNECT_TIME);
  X(CURLINFO_CERTINFO);
  X(CURLINFO_CONDITION_UNMET);

  printf("@curlinfotype\n");
  X(CURLINFO_STRING);
  X(CURLINFO_LONG);
  X(CURLINFO_DOUBLE);
  X(CURLINFO_SLIST);
  X(CURLINFO_MASK);
  X(CURLINFO_TYPEMASK);

  printf("@curliocmd\n");
  X(CURLIOCMD_NOP);
  X(CURLIOCMD_RESTARTREAD);

  printf("@curlioerr\n");
  X(CURLIOE_OK);
  X(CURLIOE_UNKNOWNCMD);
  X(CURLIOE_FAILRESTART);

  printf("@curlopttype\n");
  X(CURLOPTTYPE_LONG);
  X(CURLOPTTYPE_OBJECTPOINT);
  X(CURLOPTTYPE_FUNCTIONPOINT);
  X(CURLOPTTYPE_OFF_T);

  printf("@curlpause\n");
  X(CURLPAUSE_RECV);
  X(CURLPAUSE_RECV_CONT);
  X(CURLPAUSE_SEND);
  X(CURLPAUSE_SEND_CONT);
  X(CURLPAUSE_ALL);
  X(CURLPAUSE_CONT);

  printf("@curlsocktype\n");
  X(CURLSOCKTYPE_IPCXN);

  printf("@curlversioncodes\n");
  X(CURL_VERSION_IPV6);
  X(CURL_VERSION_KERBEROS4);
  X(CURL_VERSION_SSL);
  X(CURL_VERSION_LIBZ);
  X(CURL_VERSION_NTLM);
  X(CURL_VERSION_GSSNEGOTIATE);
  X(CURL_VERSION_DEBUG);
  X(CURL_VERSION_ASYNCHDNS);
  X(CURL_VERSION_SPNEGO);
  X(CURL_VERSION_LARGEFILE);
  X(CURL_VERSION_IDN);
  X(CURL_VERSION_SSPI);
  X(CURL_VERSION_CONV);
  X(CURL_VERSION_CURLDEBUG);

  printf("@httpversion\n");
  X(CURL_HTTP_VERSION_NONE);
  X(CURL_HTTP_VERSION_1_0);
  X(CURL_HTTP_VERSION_1_1);

  printf("@netrcoption\n");
  X(CURL_NETRC_IGNORED);
  X(CURL_NETRC_OPTIONAL);
  X(CURL_NETRC_REQUIRED);

  printf("@redirflags\n");
  X(CURL_REDIR_GET_ALL);
  X(CURL_REDIR_POST_301);
  X(CURL_REDIR_POST_302);
  X(CURL_REDIR_POST_ALL);

  printf("@sslversion\n");
  X(CURL_SSLVERSION_DEFAULT);
  X(CURL_SSLVERSION_TLSv1);
  X(CURL_SSLVERSION_SSLv2);
  X(CURL_SSLVERSION_SSLv3);

  printf("@curlproto\n");
  X(CURLPROTO_HTTP);
  X(CURLPROTO_HTTPS);
  X(CURLPROTO_FTP);
  X(CURLPROTO_FTPS);
  X(CURLPROTO_SCP);
  X(CURLPROTO_SFTP);
  X(CURLPROTO_TELNET);
  X(CURLPROTO_LDAP);
  X(CURLPROTO_LDAPS);
  X(CURLPROTO_DICT);
  X(CURLPROTO_FILE);
  X(CURLPROTO_TFTP);
  X(CURLPROTO_ALL);

  printf("@curlauth\n");
  X(CURLAUTH_NONE);
  X(CURLAUTH_BASIC);
  X(CURLAUTH_DIGEST);
  X(CURLAUTH_GSSNEGOTIATE);
  X(CURLAUTH_NTLM);
  X(CURLAUTH_DIGEST_IE);
  X(CURLAUTH_ANY);
  X(CURLAUTH_ANYSAFE);

  printf("@ipresolve\n");
  X(CURL_IPRESOLVE_WHATEVER);
  X(CURL_IPRESOLVE_V4);
  X(CURL_IPRESOLVE_V6);

  printf("@curlsshauth\n");
  X(CURLSSH_AUTH_NONE);
  X(CURLSSH_AUTH_PUBLICKEY);
  X(CURLSSH_AUTH_PASSWORD);
  X(CURLSSH_AUTH_HOST);
  X(CURLSSH_AUTH_KEYBOARD);
  X(CURLSSH_AUTH_DEFAULT);

  return 0;
}

/* Here there be dragons */