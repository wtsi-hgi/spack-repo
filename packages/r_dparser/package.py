# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDparser(RPackage):
	"""Port of 'Dparser' Package

	A Scannerless GLR parser/parser generator.  Note that GLR standing for "generalized LR", where L stands for "left-to-right" and
   R stands for "rightmost (derivation)".  For more information see <https://en.wikipedia.org/wiki/GLR_parser>. This parser is based on the Tomita
   (1987) algorithm. (Paper can be found at <https://aclanthology.org/P84-1073.pdf>).
   The original 'dparser' package documentation can be found at <https://dparser.sourceforge.net/>.  This allows you to add mini-languages to R (like
   rxode2's ODE mini-language Wang, Hallow, and James 2015 <DOI:10.1002/psp4.12052>) or to parse other languages like 'NONMEM' to automatically translate
   them to R code.   To use this in your code, add a LinkingTo dparser in your DESCRIPTION file and instead of using #include <dparse.h> use
   #include <dparser.h>.  This also provides a R-based port of the make_dparser <https://dparser.sourceforge.net/d/make_dparser.cat> command called
   mkdparser().  Additionally you can parse an arbitrary grammar within R using the dparse() function, which works on most OSes and is mainly for grammar
   testing.  The fastest parsing, of course, occurs at the C level, and is suggested.
	"""
	
	homepage = "https://nlmixr2.github.io/dparser-R/"
	cran = "dparser" 

	version("1.3.1-11", md5="aadf8e249e42956aa97b8ecf0dfaf9e0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
