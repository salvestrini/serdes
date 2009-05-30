##### http://autoconf-archive.cryp.to/ax_prog_python_modules.html
#
# SYNOPSIS
#
#   AX_PROG_PYTHON_MODULES(MODULES,[ACTION-IF-TRUE],[ACTION-IF-FALSE])
#
# This macro looks if the supplied MODULES are available under the python
# interpreter detected via AX_PROG_PYTHON macro. All log message will be dumped
# to config.log.
#
# Use it in your configure.ac as:
#
#   AX_PROG_PYTHON([OptParse ElementTree ...]),[ ... ],[ ... ])
#
# LAST MODIFICATION
#
#   2008-12-11
#
# NOTE
#   This macro is based upon AC_PROG_PERL_MODULES macro by Dean Povey
#   <povey@wedgetail.com>
#
# COPYLEFT
#
#  Copyright (c) 2008 Francesco Salvestrini <salvestrini@users.sourceforge.net>
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation; either version 2 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
#   02111-1307, USA.

AC_DEFUN([AX_PROG_PYTHON_MODULES],[
  AC_PREREQ([2.61])
  
  ac_python_modules="$1"
  
  AS_IF([test -n "$PYTHON"],[
    ac_python_modules_failed=0
    for ac_python_module in $ac_python_modules; do

      AC_MSG_CHECKING(for python module $ac_python_module)
      # Perform check and log its output to config.log
      AS_IF([AC_TRY_COMMAND($PYTHON -c "import $ac_python_module" 1>&AS_MESSAGE_LOG_FD)],[
        AC_MSG_RESULT([yes]);
      ],[
        AC_MSG_RESULT([no]);
        ac_python_modules_failed=1
      ])
    done
  
    AS_IF([test "$ac_python_modules_failed" = 0],[
      :
      $2
    ],[
      :
      $3
    ])
  ],[
    :
    $3
  ])
])
