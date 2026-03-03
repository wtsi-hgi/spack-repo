# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnmc(RPackage):
	"""Compute High Dimensional Orthant Probabilities

	Computationally efficient method to estimate orthant probabilities of high-dimensional Gaussian vectors. Further implements a function to compute conservative estimates of excursion sets under Gaussian random field priors. 
	"""
	
	homepage = "https://doi.org/10.1080/10618600.2017.1360781"
	cran = "anMC" 

	version("0.2.5", md5="786095f47ee9fa68bb232851864b40a5")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
