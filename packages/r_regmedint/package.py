# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegmedint(RPackage):
	"""Regression-Based Causal Mediation Analysis with Interaction and
Effect Modification Terms

	This is an extension of the regression-based causal mediation analysis first proposed by Valeri and VanderWeele (2013) <doi:10.1037/a0031034> and Valeri and VanderWeele (2015) <doi:10.1097/EDE.0000000000000253>). It supports including effect measure modification by covariates(treatment-covariate and mediator-covariate product terms in mediator and outcome regression models) as proposed by Li et al (2023) <doi:10.1097/EDE.0000000000001643>. It also accommodates the original 'SAS' macro and 'PROC CAUSALMED' procedure in 'SAS' when there is no effect measure modification. Linear and logistic models are supported for the mediator model. Linear, logistic, loglinear, Poisson, negative binomial, Cox, and accelerated failure time (exponential and Weibull) models are supported for the outcome model.
	"""
	
	homepage = "https://kaz-yos.github.io/regmedint/"
	cran = "regmedint" 

	version("1.0.1", md5="1855cddd0a95e21dcd926bcb43f35eb7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
