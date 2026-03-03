# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoostmlr(RPackage):
	"""Boosting for Multivariate Longitudinal Responses

	Jointly models the multivariate longitudinal responses and multiple covariates and time using gradient boosting approach.
	"""
	
	cran = "BoostMLR" 

	version("1.0.3", md5="f3a09d1b61e3ec650da8a97c35074bdb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
