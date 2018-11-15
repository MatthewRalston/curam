

VERSION       = $(shell git rev-parse --short HEAD)
DESTDIR       =
PREFIX        = /usr
SHELL         = /bin/bash
INSTALL       = /usr/bin/env install
MSGFMT        = /usr/bin/msgfmt
SED           = /bin/sed
PKGNAME	      = curam
bindir        = $(PREFIX)/bin
libdir        = $(PREFIX)/lib
sysconfdir    = etc
completiondir = ${PREFIX}/share/bash-completion/completions
localedir     = $(PREFIX)/share/locale
localstatedir = $(PREFIX)/var
mandir        = $(PREFIX)/share/man



all:
	clean
	install
	dist

docs: Makefile bin/curam
	/usr/bin/core_perl/pod2man bin/$(PKGNAME) man/$(PKGNAME).1


install: $(SCRIPTS) docs
	$(INSTALL) -d $(DESTDIR)$(bindir)
	$(INSTALL) -d $(DESTDIR)$(libdir)/$(PKGNAME)
	$(INSTALL) -d $(DESTDIR)/$(sysconfdir)/$(PKGNAME)
	$(INSTALL) -d $(DESTDIR)$(mandir)
	$(INSTALL) -d $(DESTDIR)$(completiondir)
	$(INSTALL) -d $(mandir)/man1
	# Scripts
	$(INSTALL) -m755 bin/$(PKGNAME) $(DESTDIR)$(bindir)/$(PKGNAME)
	# Libs
	$(INSTALL) -m644 lib/$(PKGNAME)/archNews.py $(DESTDIR)$(libdir)/$(PKGNAME)/archNews.py
	# Man
	$(INSTALL) -m644 man/$(PKGNAME).1 $(DESTDIR)$(mandir)/$(PKGNAME).1
	# Config files
	$(INSTALL) -m644 etc/$(PKGNAME)/$(PKGNAME).conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/$(PKGNAME).conf.defaults
	$(INSTALL) -m644 etc/$(PKGNAME)/$(PKGNAME).conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/$(PKGNAME).conf
	$(INSTALL) -m644 etc/$(PKGNAME)/home_excludes.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/home_excludes.conf.defaults
	$(INSTALL) -m644 etc/$(PKGNAME)/home_excludes.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/home_excludes.conf
	$(INSTALL) -m644 etc/$(PKGNAME)/media_excludes.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/media_excludes.conf.defaults
	$(INSTALL) -m644 etc/$(PKGNAME)/media_excludes.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/media_excludes.conf
	$(INSTALL) -m644 etc/$(PKGNAME)/os_excludes.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/os_excludes.conf.defaults
	$(INSTALL) -m644 etc/$(PKGNAME)/os_excludes.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/os_excludes.conf
	$(INSTALL) -m644 etc/$(PKGNAME)/symlinks_check.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/symlinks_check.conf.defaults
	$(INSTALL) -m644 etc/$(PKGNAME)/symlinks_check.conf.defaults $(DESTDIR)/$(sysconfdir)/$(PKGNAME)/symlinks_check.conf

dist:
	mkdir $(PKGNAME)-$(VERSION)
	cp -r AUTHORS bin etc INSTALL lib LICENSE Makefile man $(PKGNAME)-$(VERSION)
	tar -zcvf $(PKGNAME)-$(VERSION).tar.gz $(PKGNAME)-$(VERSION)
	rm -rf $(PKGNAME)-$(VERSION)


clean:
	rm -f $(PKGNAME)-$(VERSION).tar.gz
	rm -rf $(PKGNAME)-$(VERSION)

.PHONY: all install clean dist









