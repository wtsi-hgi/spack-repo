# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafd(RPackage):
	"""Statistical Analysis of Fuzzy Data

	The aim of the package is to provide some basic functions
        for doing statistics with one dimensional Fuzzy Data (in the
        form of polygonal fuzzy numbers). In particular, the package
        contains functions for the basic operations on the class of
        fuzzy numbers (sum, scalar product, mean, median, Hukuhara difference) 
        as well as for calculating (Bertoluzza) distance and sample variance. 
        Moreover a function to simulate fuzzy random variables and bootstrap tests 
        for the equality of means is included. Version 2.1 fixes some bugs
        of previous versions.
	"""
	
	cran = "SAFD" 

	version("2.1", md5="28eb29d11b33de09829a5ba37930364e")

