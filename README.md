# An interface to libcurl using ctypes

This is a Python wrapper around the libcurl C library, allowing use of the C
API via ctypes. The resulting interface is not very Pythonic, but it handles
some of the low-level details so the performance of the underlying library is
mostly preserved.
