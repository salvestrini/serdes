(h2 "DESCRIPTION")
(p "SerDes is a configuration management tool like "
   (a (@ (href "http://www.catb.org/~esr/cml2/cml2-reference.html")) "CML2")
   " or "
   (a (@ (href "http://kernel.org/doc/#kconfig")) "Linux kernel kconfig")
   ".")
(p "It uses an input description in order to know the configuration "
   "symbols and their inter-relations and outputs a script "
   "that should be shipped with a package, in order to let the user tweak "
   "the configuration parameters interactively.")
(p "SerDes should work with (and even without) the "
   (a (@ (href "http://en.wikipedia.org/wiki/Autotools")) autotools)
   ".")

(h2 "USAGE")

(h3 "Input file grammar")
(p "The complete input " (a (@ (href "./grammar.html")) "grammar") " "
   "is available.")

(h2 "COPYING")
(p "The project is licensed under the "
   (a (@ (href "http://www.gnu.org/licenses/licenses.html"))
      "GNU General Public License, version 2"))

(h2 "MAINTAINERS")
(p "Francesco Salvestrini <salvestrini AT gmail DOT com>")

(h2 "AUTHORS")
(p "Francesco Salvestrini <salvestrini AT gmail DOT com>")
(p "Alessandro Massignan <ff0000 DOT it AT gmail DOT com>")

(h2 "MAILING LISTS")
(p "The project has a single moderated mailing list, with an archive. "
   "In order to post a message to the mailing list you must be subscribed. "
   "Please consult the "
   (a (@ (href "http://lists.nongnu.org/mailman/listinfo/choicetool-generic"))
      "mailing list page")
   " for more information on subscribing to the mailing list.")

(h2 "REPORT A BUG")
(p "If you think you have found a bug then please send as complete a report "
   "as possible to "
   "<choicetool-generic AT nongnu DOT org>. "
   "An easy way to collect all the required information, such as platform and "
   "compiler, is to include in your report the config.log file available at "
   "the end of the configuration procedure.")
(p "If you have a patch for a bug that hasn't yet been fixed in "
   "the latest repository sources, please be so kind to create it using the "
   "repository sources, not the release sources.")
