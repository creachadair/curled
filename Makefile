##
## Name:     Makefile
## Purpose:  Build script for ctypes-based cURL wrapper.
## 
## Copyright (c) 2009-2010 Michael J. Fromberger, All Rights Reserved.
##

.PHONY: clean distclean

CC=gcc
CFLAGS=-Wall -ansi -pedantic -I/opt/local/include
CTARGETS=curlextract
LDFLAGS=

.c.o:
	$(CC) $(CFLAGS) -c $< -o $@

$(CTARGETS):%: %.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^

clean:
	rm -vf *.o *.pyc *.pyo *~
	rm -vfr __pycache__

distclean: clean
	rm -vf $(CTARGETS)

# Here there be dragons
