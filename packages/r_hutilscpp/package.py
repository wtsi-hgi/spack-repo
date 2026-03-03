# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHutilscpp(RPackage):
	"""Miscellaneous Functions in C++

	Provides utility functions that are simply, frequently used, 
    but may require higher performance that what can be obtained from base R.
    Incidentally provides support for 'reverse geocoding', such as matching a point
    with its nearest neighbour in another array. Used as a complement to package
    'hutils' by sacrificing compilation or installation time for higher running 
    speeds. The name is a portmanteau of the author and 'Rcpp'.
	"""
	
	homepage = "https://github.com/hughparsonage/hutilscpp"
	cran = "hutilscpp" 

	version("0.10.4", md5="2c437babed38c1bbf5a827ce0f042803")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hutils", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
