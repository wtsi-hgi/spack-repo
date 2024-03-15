# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpelling(RPackage):
	"""Tools for Spell Checking in R

	Spell checking common document formats including latex, markdown, manual pages,
    and description files. Includes utilities to automate checking of documentation and 
    vignettes as a unit test during 'R CMD check'. Both British and American English are 
    supported out of the box and other languages can be added. In addition, packages may
    define a 'wordlist' to allow custom terminology without having to abuse punctuation.
	"""
	
	homepage = "https://ropensci.r-universe.dev/spelling"
	cran = "spelling" 

	version("2.3.0", md5="375bbd00c2d9980ee78ffb834175d139")

	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-hunspell@3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
