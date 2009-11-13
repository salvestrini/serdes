# -*- python -*-

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

import sys

from   Autoconfiguration import *

debug_enabled   = False
warning_enabled = False

def error(s) :
    assert(s != None)
    assert(s != "")
    sys.stderr.write(PROGRAM_NAME + ": " + str(s) + '\n')

def warning(s) :
    assert(s != None)
    assert(s != "")
    if (warning_enabled is True) :
        sys.stdout.write(PROGRAM_NAME + ": " + str(s) + '\n')

def debug(s) :
    assert(s != None)
    assert(s != "")
    if (debug_enabled is True) :
        sys.stdout.write(PROGRAM_NAME + ": " + str(s) + '\n')

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
