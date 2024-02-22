# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmisc(RPackage):
	"""Miscellaneous Functions for Panel Data, Quantiles, and Printing
Results

	These are miscellaneous functions for working with panel data, quantiles, and printing results.  For panel data, the package includes functions for making a panel data balanced (that is, dropping missing individuals that have missing observations in any time period), converting id numbers to row numbers, and to treat repeated cross sections as panel data under the assumption of rank invariance.  For quantiles, there are functions to make distribution functions from a set of data points (this is particularly useful when a distribution function is created in several steps), to combine distribution functions based on some external weights, and to invert distribution functions.  Finally, there are several other miscellaneous functions for obtaining weighted means, weighted distribution functions, and weighted quantiles; to generate summary statistics and their differences for two groups; and to add or drop covariates from formulas.
	"""
	
	homepage = "https://bcallaway11.github.io/BMisc/"
	cran = "BMisc" 

	version("1.4.5", md5="7c6ff046d189dc7cd0b662badefd3b15")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
