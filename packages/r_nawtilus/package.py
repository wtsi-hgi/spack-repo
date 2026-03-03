# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNawtilus(RPackage):
	"""Navigated Weighting for the Inverse Probability Weighting

	Implements the navigated weighting (NAWT) proposed by Katsumata (2020)
    <arXiv:2005.10998>, which improves the inverse probability weighting by 
    utilizing estimating equations suitable for a specific pre-specified parameter 
    of interest (e.g., the average treatment effects or the average treatment 
    effects on the treated) in propensity score estimation. It includes the 
    covariate balancing propensity score proposed by Imai and Ratkovic (2014) 
    <doi:10.1111/rssb.12027>, which uses covariate balancing conditions in 
    propensity score estimation. The point estimate of the parameter of interest
    as well as coefficients for propensity score estimation and their 
    uncertainty are produced using the M-estimation. The same functions can be 
    used to estimate average outcomes in missing outcome cases.
	"""
	
	cran = "nawtilus" 

	version("0.1.4", md5="283a273c0a79706c5ef295b628536630")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
