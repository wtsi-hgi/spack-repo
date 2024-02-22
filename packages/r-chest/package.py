# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChest(RPackage):
	"""Change-in-Estimate Approach to Assess Confounding Effects

	Applies the change-in-effect estimate method to assess confounding 
    effects in medical and epidemiological research (Greenland & Pearce (2016) 
    <doi:10.1146/annurev-publhealth-031914-122559> ). It starts with a crude model 
    including only the outcome and exposure variables. At each of the subsequent 
    steps, one variable which creates the largest change among the remaining variables 
    is selected. This process is repeated until all variables have been entered into 
    the model (Wang Z. Stata Journal 2007; 7, Number 2, pp. 183–196). Currently, the 'chest' 
    package has functions for linear regression, logistic regression, negative 
    binomial regression, Cox proportional hazards model and conditional logistic 
    regression. 
	"""
	
	cran = "chest" 

	version("0.3.7", md5="ecd5377342cab96fcd1f6f17467eb3dc")

	depends_on("r@2.20:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
