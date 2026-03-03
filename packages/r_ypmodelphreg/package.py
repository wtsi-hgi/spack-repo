# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYpmodelphreg(RPackage):
	"""The Short-Term and Long-Term Hazard Ratio Model with
Proportional Adjustment

	Provides covariate-adjusted comparison of two groups of right 
    censored data, where the binary group variable has separate short-term 
    and long-term effects on the hazard function, while effects of covariates 
    such as age, blood pressure, etc. are proportional on the hazard. The model 
    was studied in Yang and Prentice (2015) <doi:10.1002/sim.6453> and it extends 
    the two sample version of the short-term and long-term hazard ratio model
    proposed in Yang and Prentice (2005) <doi:10.1093/biomet/92.1.1>. The model 
    extends the usual Cox proportional hazards model to allow more flexible 
    hazard ratio patterns, such as gradual onset of effect, diminishing effect, 
    and crossing hazard or survival functions. This package provides 
    the following: 1) point estimates and confidence intervals for model 
    parameters; 2) point estimate and confidence interval of the average hazard 
    ratio; and 3) plots of estimated hazard ratio function with point-wise and 
    simultaneous confidence bands.
	"""
	
	cran = "YPmodelPhreg" 

	version("1.0.0", md5="703b76544ee539e75e5092d8da6d2b6a")

	depends_on("r-survival", type=("build", "run"))
