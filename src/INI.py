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
import string

from   Debug      import *
from   Trace      import *
import Exceptions

class File(object) :
    class Error(Exception) :
        pass

    def __init__(self, filename = None) :
        debug("Initializing INI file instance")
        self.__values   = { }
        self.__filename = filename
        if (self.__filename != None) :
            self.load()

    def filename(self) :
        return self.__filename

    def sections(self) :
        return self.__values.keys()

    def has_section(self, section) :
        if (self.__values.has_key(section)) :
            return True
        return False

    def options(self, section) :
        return self.__values[section].keys()

    def has_option(self, section, option) :
        if (self.__values.has_key(section)) :
            if (self.__values[section].has_key(option)) :
                return True
        return False

    def add_section(self, section) :
        assert(isinstance(section, str))
        if (not self.__values.has_key(section)) :
            self.__values[section] = { }

    def remove_section(self, section) :
        assert(isinstance(section, str))
        del self.__values[section]

    def get(self, section, option, raw = None) :
        debug("Raw parameter is `" + str(raw) + "'")

        # Be kind enough
        s = string.strip(section)
        o = string.strip(option)

        try:
            return self.__values[s][o]
        except KeyError, e:
            raise Exceptions.KeyNotFound("unknown section " +
                                         "`" + s + "' " +
                                         "or option " +
                                         "`" + o + "'")

    def set(self, section, option, value) :
        assert(value != None)

        if (not self.__values.has_key(section)) :
            self.__values[section] = { }

        # Be kind enough
        s = string.strip(section)
        o = string.strip(option)

        self.__values[s][o] = value

    def clear(self) :
        self.__values.clear()

    def load(self, filename = None) :
        if (filename != None) :
            self.__filename = filename

        if (self.__filename == None) :
            raise Exceptions.MissingFilename()

        assert(isinstance(self.__filename, str))

        debug("Loading INI data from `" + self.__filename + "'")
        handle  = open(self.__filename, 'r')
        assert(handle != None)

        lines   = handle.readlines()

        loc     = 0
        section = ""
        value   = ""
        option  = ""
        for l in lines :
            # Purify input string
            l = string.strip(l)

            # Skip comments and empy lines
            if ((l == "") or (l[0] == "#")) :
                continue

            assert(len(l) > 0)

            if (l[0] == "[") :
                loc     = string.find(l, "]")
                section = l[1:loc]
                self.add_section(section)
            elif ((l[0] in string.letters) or
                  (l[0] in string.digits)) :
                loc    = string.find(l, "=")
                option = string.strip(l[0:loc])
                value  = string.strip(l[(loc + 1):])
                self.set(section, option, value)

        handle.close()

    def save(self, filename = None) :
        if (filename != None) :
            self.__filename = filename

        if (self.__filename == None) :
            raise Exceptions.MissingFilename()

        assert(isinstance(self.__filename, str))

        debug("Saving INI data to `" + self.__filename + "'")
        handle = open(self.__filename, 'w')
        assert(handle != None)

        for section in self.__values.keys() :
            handle.write(string.join(("[", section, "]", "\n"),
                                     ""))
            for option in self.__values[section].keys() :
                handle.write(option +
                             " = " +
                             str(self.__values[section][option]))
                handle.write('\n')
            handle.write('\n')

        handle.close()

# Test
if (__name__ == '__main__') :

    f = File()
    assert(f != None)

    try :
        f.add_section("test")

        f.set("test", "value1", 1)
        assert(f.get("test", "value1") == 1)

        f.set("alfa", "value2", True)
        assert(f.get("alfa", "value2") == True)
        f.set("alfa", "value2", False)
        assert(f.get("alfa", "value2") == False)

        f.set("beta", "value3", "string")
        assert(f.get("beta", "value3") == "string")
        f.set("beta", "value3", True)
        assert(f.get("beta", "value3") == True)
        f.set("beta", "value3", "string")
        assert(f.get("beta", "value3") == "string")

        assert(len(f.sections()) == 3)

        f.clear()

        assert(not f.has_section("test"))
        assert(len(f.sections()) == 0)
    except :
        sys.exit(1)

    print("X")
    debug("Test completed")
    sys.exit(0)
