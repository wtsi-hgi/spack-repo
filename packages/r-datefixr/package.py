# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatefixr(RPackage):
	"""Standardize Dates in Different Formats or with Missing Data

	There are many different formats dates are commonly
    represented with: the order of day, month, or year can differ,
    different separators ("-", "/", or whitespace) can be used, months can
    be numerical, names, or abbreviations and year given as two digits or
    four. 'datefixR' takes dates in all these different formats and
    converts them to R's built-in date class. If 'datefixR' cannot
    standardize a date, such as because it is too malformed, then the user
    is told which date cannot be standardized and the corresponding ID for
    the row. 'datefixR' also allows the imputation of missing days and
    months with user-controlled behavior.
	"""
	
	homepage = "https://docs.ropensci.org/datefixR/"
	cran = "datefixR" 

	version("1.6.1", md5="597c6dd44cd5302b5d103405fb51bcf2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
