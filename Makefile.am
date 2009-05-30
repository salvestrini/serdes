##
## Input file for automake
##
## Copyright (C) 2008, 2009 Francesco Salvestrini
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program; if not, write to the Free Software Foundation, Inc.,
## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##

include $(top_srcdir)/Makefile.sub

ACLOCAL_AMFLAGS = -I tools/autotools/m4

SUBDIRS =					\
	tools					\
	src					\
	data					\
	docs

# Base directories
TOOLSDIR   = $(top_builddir)/tools
SCRIPTSDIR = $(TOOLSDIR)/scripts

##
## NOTE:
##     Options listed in AUTOMAKE_OPTIONS variable are applied on a
##     per-`Makefile' basis.
##
AUTOMAKE_OPTIONS = check-news

##
## NOTE:
##     Makefile.sub is automatically distributed by automake rules
##
EXTRA_DIST =							\
	BUGS TODO README NEWS COPYING AUTHORS INSTALL THANKS	\
	bootstrap						\
	configure.ac.in						\
	.todo

##
## Maintainer related targets
##

DNT_DB = $(top_srcdir)/.dnt.db
TODO: $(DNT_DB)
	$(DNT) --database=$(DNT_DB)		\
	       --mono				\
	       dump				\
	       --format="* %t"			\
	       --width=0			\
	       --filter=not-done		\
	       --output=TODO || {		\
		rm -f TODO ;			\
		exit 1 ;			\
	}

announcement:
	$(ANNOUNCE_GEN)				\
	  --release-type=alpha			\
	  --package=$(PACKAGE_TARNAME)		\
	  --prev=$(PACKAGE_VERSION).test	\
	  --curr=$(PACKAGE_VERSION)		\
	  --gpg-key-id=TEST			\
	  --url-dir=TEST

dist-hook:
	$(GITLOG_TO_CHANGELOG) > $(distdir)/ChangeLog || {	\
		rm -f ChangeLog ;				\
		exit 1 ;					\
	}

site: all
	(cd site && $(MAKE) $(AM_MAKEFLAGS) site)

HOST = "http://git.savannah.gnu.org/gitweb/?p=gnulib.git;a=blob_plain;hb=HEAD;f="

update-download:
	rm -r -f fetch-dir && \
	mkdir fetch-dir && \
	$(FETCH) $(HOST)doc/INSTALL fetch-dir/INSTALL && \
	chmod a+r fetch-dir/INSTALL && \
	chmod u+w fetch-dir/INSTALL && \
	$(FETCH) $(HOST)doc/COPYINGv2 fetch-dir/COPYING && \
	chmod a+r fetch-dir/COPYING && \
	chmod u+w fetch-dir/COPYING && \
	mv -f fetch-dir/* ./ || { \
		rm -r -f fetch-dir ; \
		exit 1 ; \
	} && \
	rm -r -f fetch-dir

update-local: Makefile update-download

maintainer-check-local: Makefile
