# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpm(RPackage):
	"""Dynamic Panel Models Fit with Maximum Likelihood

	Implements the dynamic panel models described by Allison, Williams,
 and Moral-Benito (2017 <doi:10.1177/2378023117710578>) in R. 
 This class of models uses structural equation modeling to specify dynamic 
 (lagged dependent variable) models with fixed effects for panel data. 
 Additionally, models may have predictors that are only weakly exogenous, i.e.,
 are affected by prior values of the dependent variable. Options also allow for
 random effects, dropping the lagged dependent variable, and a number of other 
 specification choices.
	"""
	
	homepage = "https://github.com/jacob-long/dpm"
	cran = "dpm" 

	version("1.2.0", md5="407976b6f9e0784b146e0d328c057cb2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-panelr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-jtools@2.0.1:", type=("build", "run"))
