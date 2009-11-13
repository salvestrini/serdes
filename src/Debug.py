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
import os
import traceback

#
# NOTE:
#     Do not include Config here in order to avoid a mutual inclusion between
#     Config and Debug (see the last lines)
#
from   Trace import *

#def _stack_dump() :
#    traceback.print_stack(file)

#def _stack_dump() :
#    type, value, tb = sys.exc_info()
#    stack = traceback.extract_tb(tb)
#
#    if (len(stack) > 0) :
#        error("Backtrace (most recent call last):")
#        for (filename, line_number, function_name, text) in stack:
#            error("  File \"%s\", line %s, in %s"
#                  %(filename, line_number, function_name))
#            error("    %s"
#                  %(text))
#    else :
#        error("No backtrace available !")

def _stack_dump(shortcut = True) :
    stack = traceback.extract_stack()

    if (len(stack) >= 0) :
        error("Stack backtrace:")

        frame_no = 0
        for (filename, line_number, function_name, text) in stack:
            if (shortcut is True) :
                # Avoid dumping past bug() or bug_on()
                if ((function_name == "bug") or (function_name == "bug_on")) :
                    error("  %s - ... Useless internals follow ..."
                          %(str(frame_no)))
                    return
            error("  %s - File \"%s\", line %s, in %s"
                  %(str(frame_no), filename, line_number, function_name))
            error("    %s"
                  %(text))
            frame_no = frame_no + 1
    else :
        error("No stack backtrace available !")

_bug_in_progress = False

def bug(s = "") :
    global _bug_in_progress

    if (_bug_in_progress) :
        error("Bug in progress while dumping a bug ...")
        return

    _bug_in_progress = True

    tmp1 = "Bug hit"
    if s != "" :
        tmp2 = tmp1 + ": " + s
    else :
        tmp2 = tmp1 + "!"
    error(tmp2)

    _stack_dump(False)

    error("Please report to <" + PACKAGE_BUGREPORT + ">")

    _bug_in_progress = False

    # NOTE:
    #     In order to detect bugs in our regression tests we must exit
    #     with an error code which differs from 77 (automake skip test) and
    #     +1/-1. We deliberately choose 33

    # Like _exit(), exit immediately ...
    os._exit(33)

def bug_on(v) :
    if (v is True) :
        bug("Unsatisfied expression " + str(v))

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
