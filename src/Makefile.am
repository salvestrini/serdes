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

bin_SCRIPTS =					\
	idlgen
EXTRA_DIST  =

plydir = $(pkgvpythondir)/ply

ply_SRCS =					\
	ply/__init__.py				\
	ply/cpp.py				\
	ply/ctokens.py				\
	ply/lex.py				\
	ply/yacc.py

ply_PYTHON =					\
	$(ply_SRCS)

EXTRA_DIST +=					\
	ply/README

pkgvpython_PYTHON =				\
	__init__.py				\
	Configuration.py			\
	INI.py					\
	Trace.py				\
	Exceptions.py				\
	Command.py				\
	Debug.py

nodist_pkgvpython_PYTHON =			\
	Autoconfiguration.py

BUILT_SOURCES =					\
	Autoconfiguration.py

## NOTE: The following variable is used by maintainer-check-local target
OUR_PYTHON_SRCS =				\
	$(pkgvpython_PYTHON)			\
	$(nodist_pkgvpython_PYTHON)		\
	$(commands_PYTHON)

CLEANFILES =					\
	$(nodist_pkgvpython_PYTHON)		\
	$(bin_SCRIPTS)				\
	*.pyc					\
	*.pyo					\
	ply/*.pyc				\
	ply/*.pyo

idlgen: $(srcdir)/idlgen.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/idlgen.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
		rm -f $@ $@.tmp ; \
		exit 1 ; \
	}
EXTRA_DIST += idlgen.in

Autoconfiguration.py: $(srcdir)/Autoconfiguration.py.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/Autoconfiguration.py.in > $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
		rm -f $@ $@.tmp ; \
		exit 1 ; \
	}
EXTRA_DIST += Autoconfiguration.py.in

##
## Local check target
##
check-local: Makefile
	for i in $(pkgvpython_PYTHON) ; do \
		m=`echo $$i | $(SED) -e 's,\.py,,'` && \
		rm -f $$m.pyc && \
		echo $(ECHO_N) "checking module $$m ($$i)... $(ECHO_C)" && \
		PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(srcdir)@PATH_SEPARATOR@$(builddir) $(PYTHON) $(srcdir)/$$i > test.log 2>&1 || { \
			echo "$(ECHO_T)no" ; \
			cat test.log ; \
			exit 1 ; \
		} ; \
		echo "$(ECHO_T)yes" ; \
	done
	for i in $(commands_PYTHON) ; do \
		m=`echo $$i | $(SED) -e 's,\.py,,'` && \
		rm -f $$m.pyc && \
		echo $(ECHO_N) "checking module $$m ($$i)... $(ECHO_C)" && \
		PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(srcdir)@PATH_SEPARATOR@$(builddir) $(PYTHON) $(srcdir)/$$i > test.log 2>&1 || { \
			echo "$(ECHO_T)no" ; \
			cat test.log ; \
			exit 1 ; \
		} ; \
		echo "$(ECHO_T)yes" ; \
	done
	for i in $(nodist_pkgvpython_PYTHON) ; do \
		m=`echo $$i | $(SED) -e 's,\.py,,'` && \
		rm -f $$m.pyc && \
		echo $(ECHO_N) "checking module $$m ($$i)... $(ECHO_C)" && \
		PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(srcdir)@PATH_SEPARATOR@$(builddir) $(PYTHON) $(builddir)/$$i > test.log 2>&1 || { \
			echo "$(ECHO_T)no" ; \
			cat test.log ; \
			exit 1 ; \
		} ; \
		echo "$(ECHO_T)yes" ; \
	done
	rm -f test.log

CLEANFILES += test.log

##
## XXX FIXME:
##     Replace 'sed' with '$SED' in install-exec-hook and uninstall-hook
##     rules ...
##

## Make versioned links on bin_SCRIPTS.  We only run the transform on the
## root name; then we make a versioned link with the transformed base name.
## This seemed like the most reasonable approach.
install-exec-hook:
	for p in $(bin_SCRIPTS); do \
	  f="`echo $$p|sed '$(transform)'`"; \
	  fv="$$f-$(PACKAGE_API)"; \
	  cd $(DESTDIR)$(bindir) && \
	  rm -f $$fv && \
	  mv -f $$f $$fv && \
	  $(LN_S) $$fv $$f; \
	done

uninstall-hook:
	for p in $(bin_SCRIPTS); do \
	  f="`echo $$p|sed '$(transform)'`"; \
	  fv="$$f-$(PACKAGE_API)"; \
	  rm -f $(DESTDIR)$(bindir)/$$fv; \
	done

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-parameters: Makefile $(bin_SCRIPTS)
	for i in $(bin_SCRIPTS) ; do \
		echo @ECHO_N@ "Checking standard parameters for $$i... " ; \
		if ( ./$$i -h 2>&1 > /dev/null ) ; then \
			echo "@ECHO_T@ok" ; \
		else \
			echo "@ECHO_T@error" ; \
			exit 1 ; \
		fi ; \
	done

PYCHECKER_FLAGS = --stdlib --limit 50 --maxlines 260

maintainer-check-python: Makefile $(OUR_PYTHON_SRCS)
	$(PYCHECKER) $(PYCHECKER_FLAGS) $(OUR_PYTHON_SRCS)

maintainer-check-whitespaces: Makefile $(OUR_PYTHON_SRCS)
	$(WHITESPACE_DETECT) $(OUR_PYTHON_SRCS)

maintainer-check-wordwraps: Makefile $(OUR_PYTHON_SRCS)
	$(WORDWRAP_DETECT) $(OUR_PYTHON_SRCS)

maintainer-check-local: Makefile		\
	maintainer-check-whitespaces		\
	maintainer-check-wordwraps		\
	maintainer-check-python			\
	maintainer-check-parameters
