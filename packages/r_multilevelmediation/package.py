# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilevelmediation(RPackage):
	"""Utility Functions for Multilevel Mediation Analysis

	The ultimate goal is to support 2-2-1, 2-1-1, and 1-1-1 models for
 multilevel mediation, the option of a moderating variable for either the a, b,
 or both paths, and covariates. Currently the 1-1-1 model is supported
 and several options of random effects; the initial code for bootstrapping was
 evaluated in simulations by Falk, Vogel, Hammami, and Miočević (2024) <doi:10.3758/s13428-023-02079-4>.
 Support for Bayesian estimation using 'brms' comprises ongoing work. Currently
 only continuous mediators and outcomes are supported. Factors for any
 predictors must be numerically represented.
	"""
	
	cran = "multilevelmediation" 

	version("0.3.1", md5="c0856c09edd7e69d225a4ce3ac1ef190")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
