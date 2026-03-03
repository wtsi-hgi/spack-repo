# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreekletters(RPackage):
	"""Routines for Writing Greek Letters and Mathematical Symbols on
the 'RStudio' and 'RGui'

	An implementation of functions to display Greek letters on the 'RStudio' (include subscript and superscript indexes) and 'RGui' (without subscripts and only with superscript 1, 2 or 3; because 'RGui' doesn't support printing the corresponding Unicode characters as a string: all subscripts ranging from 0 to 9 and superscripts equal to 0, 4, 5, 6, 7, 8 or 9). The functions in this package do not work properly on the R console. Characters are used via Unicode and encoded as UTF-8 to ensure that they can be viewed on all operating systems. Other characters related to mathematics are included, such as the infinity symbol. All this accessible from very simple commands. This is a package that can be used for teaching purposes, the statistical notation for hypothesis testing can be written from this package and so it is possible to build a course from the 'swirlify' package. Another utility of this package is to create new summary functions that contain the functional form of the model adjusted with the Greek letters, thus making the transition from statistical theory to practice easier. In addition, it is a natural extension of the 'clisymbols' package.
	"""
	
	cran = "greekLetters" 

	version("1.0.2", md5="6802970cfddfa0e300ae73533eacfc2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
