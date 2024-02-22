# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariancegamma(RPackage):
	"""The Variance Gamma Distribution

	Provides functions for the variance gamma
        distribution. Density, distribution and quantile functions.
        Functions for random number generation and fitting of the
        variance gamma to data. Also, functions for computing moments
        of the variance gamma distribution of any order about any
        location. In addition, there are functions for checking the
        validity of parameters and to interchange different sets of
        parameterizations for the variance gamma distribution.
	"""
	
	cran = "VarianceGamma" 

	version("0.4-2", md5="3ce8b9f67752ad2aa915b0f89550c931")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-distributionutils", type=("build", "run"))
	depends_on("r-generalizedhyperbolic", type=("build", "run"))
