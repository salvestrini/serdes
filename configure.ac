# Process this file with autoconf to produce a configure script.

#
# configure.ac for idlgen
#
# Copyright (C) 2008, 2009 Francesco Salvestrini
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

AC_INIT([SerDes],
        m4_esyscmd([tools/maint/git-version-gen .tarball-version]),
        [salvestrini@gmail.com],
        [serdes],
        [http://github.com/salvestrini/boar])

# Check for a recent version of autoconf
AC_PREREQ([2.64])

# Place/find all autotools related files in the following directories
AC_CONFIG_AUX_DIR([tools/autotools])
AC_CONFIG_MACRO_DIR([tools/autotools/m4])
AC_CONFIG_SRCDIR([src/idlgen.in])

#
# For automake options (AM_INIT_AUTOMAKE options) see Makefile.am
# file, AUTOMAKE_OPTIONS variable
#
AM_INIT_AUTOMAKE([1.10 foreign std-options -Wall])

#
# Build related programs
#
AC_PROG_INSTALL
AC_PROG_MAKE_SET
AC_PROG_LN_S
AC_PROG_MKDIR_P
AC_PROG_GREP
AC_PROG_SED
AC_PROG_AWK

AX_PATH_MISSING([HELP2MAN],       [help2man])
AX_PATH_MISSING([SITETOOL],       [sitetool])
AX_PATH_MISSING([WGET],           [wget])
AX_PATH_MISSING([DNT],            [dnt])
AX_PATH_MISSING([DEVTODO_TO_DNT], [devtodo-to-dnt])
AX_PATH_MISSING([PERL],           [perl])
AX_PATH_MISSING([PYCHECKER],      [pychecker])

#
# Runtime related programs
#
AM_PATH_PYTHON([2.5],[:],
	AC_MSG_ERROR([Missing required Python interpreter])
])
PYTHON_AUTOFRISK_CHECKS
PYTHON_AUTOFRISK_SUMMARY

AC_PATH_PROG([OMNIIDL], [omniidl])
AS_IF([test -z "$OMNIIDL"],[
	AC_MSG_ERROR([Missing required omniidl program])
])

#
# The API version is the base version.  We must guarantee
# compatibility for all releases with the same API version.
# Our current rule is that:
#
# * All releases, including the prereleases, in an X.Y series
#   are compatible.  So 1.5.1 is compatible with 1.5.
#
# * Prereleases on the trunk are all incompatible -- 1.5.1 and 1.5.2
#   aren't the same.
#
AX_SPLIT_VERSION($PACKAGE_VERSION)
API_VERSION="${AX_MAJOR_VERSION}.${AX_MINOR_VERSION}"
AC_SUBST(API_VERSION)

# Versioned directories, defined here for convenience
AC_SUBST(pkgvdir,       ["\${datadir}/${PACKAGE}-${API_VERSION}"])
AC_SUBST(pkgvbindir,    ["\${datadir}/${PACKAGE}-${API_VERSION}/bin"])
AC_SUBST(pkgvdatadir,   ["\${datadir}/${PACKAGE}-${API_VERSION}/data"])
AC_SUBST(pkgvlibsdir,   ["\${datadir}/${PACKAGE}-${API_VERSION}/libs"])
AC_SUBST(pkgvpythondir, ["\${pythondir}/${PACKAGE}-${API_VERSION}"])

AC_CONFIG_FILES([
	Makefile

	docs/Makefile

	src/Makefile

	data/Makefile

	site/Makefile
	site/in/Makefile

	tools/Makefile
	tools/maint/Makefile
	tools/autotools/Makefile
	tools/autotools/m4/Makefile
])

AC_CONFIG_FILES([tools/maint/fetch],               [chmod +x tools/maint/fetch])
AC_CONFIG_FILES([tools/maint/whitespace-detect],   [chmod +x tools/maint/whitespace-detect])
AC_CONFIG_FILES([tools/maint/gitlog-to-committers],[chmod +x tools/maint/gitlog-to-committers])
AC_CONFIG_FILES([tools/maint/gittag-to-date],      [chmod +x tools/maint/gittag-to-date])

AC_OUTPUT