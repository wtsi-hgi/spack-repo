# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQbld(RPackage):
	"""Quantile Regression for Binary Longitudinal Data

	Implements the Bayesian quantile regression model for binary longitudinal data 
             (QBLD) developed in Rahman and Vossmeyer (2019) <DOI:10.1108/S0731-90532019000040B009>.
             The model handles both fixed and random effects and implements both a blocked
             and an unblocked Gibbs sampler for posterior inference.
	"""
	
	cran = "qbld" 

	version("1.0.3", md5="6a25a6d7d68f0f6d5c1e106f76ac68e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-stablegr", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
