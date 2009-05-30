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
import ConfigParser

from   Autoconfiguration import *

_DB_FILE_TPL      = PROGRAM_NAME + ".db"
_CFG_FILE_TPL     = PROGRAM_NAME + ".cfg"

DEFAULT_DB_FILE   = "." + _DB_FILE_TPL
DEFAULT_CFG_FILE  = "." + _CFG_FILE_TPL

# Search paths we look into for the configuration files
CFG_SEARCH_PATHS  = [ '@sysconfdir@/' + _CFG_FILE_TPL,
                      '$HOME/.'       + _CFG_FILE_TPL ]

class Configuration(ConfigParser.ConfigParser) :
    __modified = False

    def set(self, section, option, value) :
        ConfigParser.ConfigParser.set(self, section, option, value)
        self.__modified = True

    def modified(self) :
        return self.__modified

    def clean(self) :
        self.__modified = False

# Test
if (__name__ == '__main__') :
    c = Configuration()

    sys.exit(0)
