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
import exceptions

from   Debug import *
from   Trace import *

#
# NOTE:
#     The base exception class assert() for message != None, in order to avoid
#     unnecessary assert() calls
#
class EBase(Exception) :
    def __init__(self, message) :
        assert(message != None)
        assert(type(message) == str)
        self.__message = message

    def __str__(self) :
        return self.__message

    __repr__ = __str__

#
# OS related exceptions
#
class EOS(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

#
# Time related exceptions
#
class ETime(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class WrongTimeFormat(ETime) :
    def __init__(self, message) :
        ETime.__init__(self, "wrong time format `" + message + "'")

#
# Priority related exceptions
#
class EPriority(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class UnknownPriority(EPriority):
    def __init__(self, message) :
        EPriority.__init__(self, "unknown priority `" + message + "'")

#
# Database related exceptions
#
class EDatabase(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class UnknownElement(EDatabase):
    def __init__(self, message) :
        EDatabase.__init__(self, "unknown element `" + message + "'")

class MissingDatabase(EDatabase):
    def __init__(self, message) :
        EDatabase.__init__(self,
                           "missing database "
                           "`" + message + "' "
                           ", try initializing or importing")

class MalformedDatabase(EDatabase):
    def __init__(self, message = None) :
        tmp = ""
        if (message != None) :
            tmp = " `" + message + "'"
        EDatabase.__init__(self, "malformed database" + tmp)

class CorruptedDatabase(EDatabase):
    def __init__(self, message) :
        EDatabase.__init__(self,
                           "database "
                           "`" + message + "' "
                           "is corrupted")

class ProblemsReading(EDatabase):
    def __init__(self, name, message) :
        tmp = ""
        if (message != None) :
            tmp = ", " + message
        EDatabase.__init__(self,
                           "problems reading database "
                           "`" + name + "'" + tmp)

class ProblemsWriting(EDatabase):
    def __init__(self, name, message) :
        tmp = ""
        if (message != None) :
            tmp = ", " + message
        EDatabase.__init__(self,
                           "problems writing database "
                           "`" + name + "'" + tmp)

#
# File related exceptions
#
class EFile(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class CannotWrite(EFile):
    def __init__(self, message) :
        EFile.__init__(self, "cannot write to file `" + message + "'")

class CannotRead(EFile):
    def __init__(self, message) :
        EFile.__init__(self, "cannot read from file `" + message + "'")

#
# ID related exceptions
#
class EID(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class MalformedId(EID):
    def __init__(self, message) :
        EID.__init__(self, message)

class Parentless(EID):
    def __init__(self, message) :
        EID.__init__(self, "node `" + message + "' is parentless")

#
# Configuration related exceptions
#
class EConfiguration(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class UnknownSection(EConfiguration):
    def __init__(self, message) :
        EConfiguration.__init__(self,
                                "unknown section "
                                "`" + message + "' "
                                "in configuration")

class MissingSection(EConfiguration):
    def __init__(self, message) :
        EConfiguration.__init__(self, "missing section")

class MissingKey(EConfiguration):
    def __init__(self, message) :
        EConfiguration.__init__(self, "missing key")

class UnknownKey(EConfiguration):
    def __init__(self, message) :
        EConfiguration.__init__(self,
                                "unknown key "
                                "`" + message + "' "
                                "in configuration")

#
# Parameters related exceptions
#

class EParameters(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class ExplicitExit(EParameters) :
    def __init__(self, message, code) :
        assert(code != None)
        assert(type(code) == int)

        #
        # NOTE:
        #     Empty messages are allowed for exit code == 0 (message is
        #     useless)
        #
        if (code == 0) :
            message = ""

        EParameters.__init__(self, message)
        self.__code = code

    # XXX FIXME:
    #     We need to change the str() nethod due to the SystemException str()
    #     different behavior
    def __str__(self) :
        return "explicit exit with code " + str(self.__code)

    def code(self) :
        return self.__code

class MissingParameters(EParameters):
    def __init__(self, message = "parameter(s)") :
        EParameters.__init__(self, "missing " + message)

class TooManyParameters(EParameters):
    def __init__(self) :
        EParameters.__init__(self, "too many parameter(s)")

class UnknownArgument(EParameters):
    def __init__(self) :
        EParameters.__init__(self, "unknown argument")

class UnknownParameter(EParameters):
    def __init__(self, message) :
        EParameters.__init__(self, "unknown parameter `" + message + "'")

class WrongParameter(EParameters):
    def __init__(self, message = None) :
        s = ""
        if (message != None) :
            s = ", " + message
        EParameters.__init__(self, "wrong parameter" + s)

class ForceNeeded(EParameters):
    def __init__(self, message) :
        EParameters.__init__(self, message + ", use `--force' to override")

#
# Tree related exceptions
#
class ETree(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class NodeUnavailable(ETree):
    def __init__(self, message) :
        ETree.__init__(self, "cannot find node `" + message + "'")

#
# Stack related exceptions
#
class EStack(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class EmptyStack(EStack):
    def __init__(self) :
        EStack.__init__(self, "stack is empty")

#
# Filter related exceptions
#
class EFilter(EBase):
    def __init__(self, message) :
        EBase.__init__(self, message)

class UnknownFilter(EFilter):
    def __init__(self, message) :
        EFilter.__init__(self, "unknown filter `" + message + "'")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
