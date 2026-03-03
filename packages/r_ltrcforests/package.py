# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtrcforests(RPackage):
	"""Ensemble Methods for Survival Data with Time-Varying Covariates

	Implements the conditional inference forest and relative risk forest 
             algorithm to modeling left-truncated right-censored data with time-invariant        
             covariates, and (left-truncated) right-censored survival data with time-varying 
             covariates. It also provides functions to tune the parameters and evaluate the 
             model fit. See Yao et al. (2022) <doi:10.1177/09622802221111549>.
	"""
	
	cran = "LTRCforests" 

	version("0.7.0", md5="9842b9357b89ddd4c5508ae19c9a5f84")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
