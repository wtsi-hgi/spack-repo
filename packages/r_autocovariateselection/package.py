# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutocovariateselection(RPackage):
	"""Automated Covariate Selection Using HDPS Algorithm

	Contains functions to implement automated covariate selection using methods described in the
             high-dimensional propensity score (HDPS) algorithm by Schneeweiss et.al. Covariate adjustment in real-world-observational-data (RWD) is important for
             for estimating adjusted outcomes and this can be done by using methods such as, but not limited to, propensity score 
             matching, propensity score weighting and regression analysis. While these methods strive to statistically adjust for 
             confounding, the major challenge is in selecting the potential covariates that can bias the outcomes comparison estimates 
             in observational RWD (Real-World-Data). This is where the utility of automated covariate selection comes in. 
             The functions in this package help to implement the three major steps of automated covariate selection as described by
             Schneeweiss et. al elsewhere. These three functions, in order of the steps required to execute automated covariate 
             selection are, get_candidate_covariates(), get_recurrence_covariates() and get_prioritised_covariates(). 
             In addition to these functions, a sample real-world-data from publicly available de-identified medical claims data is 
             also available for running examples and also for further exploration. The original article where the algorithm is described 
             by Schneeweiss et.al. (2009) <doi:10.1097/EDE.0b013e3181a663cc> .
	"""
	
	homepage = "https://github.com/technOslerphile/autoCovariateSelection"
	cran = "autoCovariateSelection" 

	version("1.0.0", md5="08e4d728fcf31f398c2fe419c34ef3a0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
