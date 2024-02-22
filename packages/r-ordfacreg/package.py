# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdfacreg(RPackage):
	"""Least Squares, Logistic, and Cox-Regression with Ordered
Predictors

	In biomedical studies, researchers are often interested in assessing the association between one or more ordinal explanatory variables and an outcome variable, at the same time adjusting for covariates of any type. The outcome variable may be continuous, binary, or represent censored survival times. In the absence of a precise knowledge of the response function, using monotonicity constraints on the ordinal variables improves efficiency in estimating parameters, especially when sample sizes are small. This package implements an active set algorithm that efficiently computes such estimators.
	"""
	
	homepage = "http://www.kasparrufibach.ch"
	cran = "OrdFacReg" 

	version("1.0.6", md5="19f591578e2fa49223d84ce5aa08db3d")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-eha", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
