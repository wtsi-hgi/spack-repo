# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinreginteractive(RPackage):
	"""Interactive Interpretation of Linear Regression Models

	Interactive visualization of effects, response functions 
    and marginal effects for different kinds of regression models. In this version 
    linear regression models, generalized linear models, generalized additive
    models and linear mixed-effects models are supported.  
    Major features are the interactive approach and the handling of the effects of categorical covariates: 
    if two or more factors are used as covariates every combination of the levels of each 
    factor is treated separately. The automatic calculation of 
    marginal effects and a number of possibilities to customize the graphical output 
    are useful features as well.
	"""
	
	cran = "LinRegInteractive" 

	version("0.3-3", md5="e9b1e11458e8d2d3e2eeef9e72b0f19a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rpanel@1.1.4:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
