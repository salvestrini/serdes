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
from   optparse   import OptionParser
#import textwrap
import string

from   Trace      import *
from   Debug      import *
import Exceptions

class Command(OptionParser, object) :
    # NOTE: An empty string is an allowed name (main uses it)
    def __init__(self, name, format = "[OPTION]...", footer = []) :
        assert(name != None)
        assert(isinstance(name, str))
        assert(format != None)
        assert(isinstance(format, str))
        assert(footer != None)
        assert(isinstance(footer, list))

        self.__name   = name

        # Build footer as a string
        tmp = ""
        if (len(footer) > 0) :
            for i in range(0, len(footer)) :
                assert(isinstance(footer[i], str))
                tmp = tmp + footer[i]
                if (i != (len(footer) - 1)) :
                    tmp = tmp + "\n"
        self.__footer = tmp

        # XXX FIXME: This is really awful ...
        if (self.__name == "") :
            usage_format   = "Usage: %prog " + format
            version_format = "%prog " + \
                "(" + PACKAGE_NAME + " " + PACKAGE_VERSION + ")"
        else :
            usage_format   = "Usage: %prog " + self.__name + " " + format
            version_format = "%prog " + self.__name + " " + \
                "(" + PACKAGE_NAME + " " + PACKAGE_VERSION + ")"

        OptionParser.__init__(self,
                              prog    = PROGRAM_NAME,
                              usage   = usage_format,
                              version = version_format,
                              #epilog  = self.__footer
                              )
        OptionParser.disable_interspersed_args(self)

    def authors(self) :
        bug("No authors() method provided by the derived class")

    # Override OptParse print_version() method
    def print_version(self, file = None) :
        OptionParser.print_version(self, file)

        assert(hasattr(self, "authors"))
        assert(callable(self.authors))
        assert(isinstance(self.authors(), list))

        print >> file, ""
        j = 0
        for i in self.authors() :
            if (j == 0) :
                header = "Copyright (C) 2008, 2009 "
            else :
                header = "                         "
            print >> file, header + i
            j = j + 1
        print >> file, ""

        print >> file, "This is free software.  You may redistribute copies of it under the terms of"
        print >> file, "the GNU General Public License <http://www.gnu.org/licenses/gpl.html>."
        print >> file, "There is NO WARRANTY, to the extent permitted by law."


    def name_get(self) :
        # Give the caller a copy of our internal data ...
        return str(self.__name)
    def name_set(self, n) :
        assert(isinstance(n, str))
        assert(n != "")
        assert(n != None)
        assert(n == string.strip(n))

        self.__name = n

    name = property(name_get, name_set, None, None)

    # Override OptParse print_help() method
    def print_help(self, file = sys.stdout) :
        # Force output to stdout
        OptionParser.print_help(self, file)
        file.write("\n")
        if (self.__footer != "") :
            file.write(self.__footer + "\n")
            file.write("\n")
        file.write("Report bugs to <" + PACKAGE_BUGREPORT + ">\n")

    # Override OptParse error() method
    def error(self, msg) :
        raise Exceptions.EParameters(msg)

    def exit(self, status = 0, msg = None):
        debug("Explicit exit called from command")
        try :
            OptionParser.exit(self, status, msg)
        except SystemExit, e :
            # Wrapping SistemExit exception with our own exception
            raise Exceptions.ExplicitExit(e, e.code)
        except :
            bug("Unhandled exception in option parser")

    ## This method should be provided by the subclass
    #def short_help(self) :
    #    bug()

    ## This method must be provided by the subclass
    #def authors(self) :
    #    bug()

    ## This method should be provided by the subclass
    #def do(self, configuration, arguments) :
    #    bug()

# Test
if (__name__ == '__main__') :

    a = Command("test")
    b = Command("test", "")
    c = Command("test", "test")
    d = Command("test", "", [])
    e = Command("test", "test", [ "" ])
    f = Command("test", "test", [ "test1" ])
    g = Command("test", "test", [ "test1", "test2" ])
    g = Command("test", "test", [ "test1", "", "test2"])

    debug("Test completed")
    sys.exit(0)
