# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlqrfe(RPackage):
	"""Adaptive Lasso Quantile Regression with Fixed Effects

	Quantile regression with fixed effects solves longitudinal data, considering the individual intercepts as fixed effects. The parametric set of this type of problem used to be huge. Thus penalized methods such as Lasso are currently applied. Adaptive Lasso presents oracle proprieties, which include Gaussianity and correct model selection. Bayesian information criteria (BIC) estimates the optimal tuning parameter lambda. Plot tools are also available.
	"""
	
	cran = "alqrfe" 

	version("1.1", md5="69d6b5de7b08cfa3970509a5e84da9d5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass@7.3.49:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
