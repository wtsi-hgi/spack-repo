# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdbrr(RPackage):
	"""High Dimensional Bayesian Ridge Regression without MCMC

	Ridge regression provide biased estimators of the regression parameters with lower variance. The HDBRR ("High Dimensional Bayesian Ridge Regression") function fits Bayesian Ridge regression without MCMC, this one uses the SVD or QR decomposition for the posterior computation.
	"""
	
	cran = "HDBRR" 

	version("1.1.4", md5="69d948e5404de22d0b8071822b0e8d0f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-bigstatsr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
