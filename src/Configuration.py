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

from   Debug             import *
from   Trace             import *
from   Autoconfiguration import *
import Exceptions
import INI

_DB_FILE_TPL      = PROGRAM_NAME + ".db"
_CFG_FILE_TPL     = PROGRAM_NAME + ".cfg"

DEFAULT_DB_FILE   = "." + _DB_FILE_TPL
DEFAULT_CFG_FILE  = "." + _CFG_FILE_TPL

# Search paths we look into for the configuration files
CFG_SEARCH_PATHS  = [ SYSCONFDIR + '/' +       _CFG_FILE_TPL,
                      '$HOME'    + '/' + '.' + _CFG_FILE_TPL ]

class Configuration(INI.File) :
    class Error(Exception) :
        pass

    class ParsingError(Error) :
        def __init__(self, message) :
            assert(message != None)
            assert(isinstance(message, str))
            self.__message = message

        def __str__(self) :
            return self.__message

        __repr__ = __str__

    def __init__(self) :
        self.__modified = False
        super(Configuration, self).__init__()

    def set(self, section, option, value) :
        super(Configuration, self).set(section, option, value)
        self.__modified = True

    def get(self, section, option, raw = None) :
        return super(Configuration, self).get(section, option, raw)

    def add_section(self, section) :
        super(Configuration, self).add_section(section)

    # This is a wrapper, please remove ASAP
    def read(self, filenames) :
        assert(isinstance(filenames, list))

        read_files = [ ]
        for i in filenames :
            if (os.path.isfile(i)) :
                try :
                    super(Configuration, self).load(i)
                    read_files.append(i)
                except Exception, e :
                    raise self.ParsingError(str(e) + " " + i)

        return read_files

    def modified_get(self) :
        return self.__modified

    modified = property(modified_get, None, None, None)

    def clean(self) :
        self.__modified = False

# Test
if (__name__ == '__main__') :
    c = Configuration()

    assert(c.modified is False)

    try :
        c.add_section("test")
        c.set("test", "value1", 1)
        c.set("test", "value2", True)
        c.set("test", "value3", "string")
    except :
        sys.exit(1)

    assert(c.modified is True)

    sys.exit(0)
