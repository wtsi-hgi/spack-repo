# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPheno(RPackage):
	"""Auxiliary Functions for Phenological Data Analysis

	Provides some easy-to-use functions for time series
        analyses of (plant-) phenological data sets. These functions
        mainly deal with the estimation of combined phenological time
        series and are usually wrappers for functions that are already
        implemented in other R packages adapted to the special
        structure of phenological data and the needs of phenologists.
        Some date conversion functions to handle Julian dates are also
        provided.
	"""
	
	cran = "pheno" 

	version("1.7-0", md5="0342dab635146ada691d9f98b6660ad9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
