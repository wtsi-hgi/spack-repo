# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowersurvepi(RPackage):
	"""Power and Sample Size Calculation for Survival Analysis of
Epidemiological Studies

	Functions to calculate power and
                sample size for testing main effect or interaction effect in
                the survival analysis of epidemiological studies
                (non-randomized studies), taking into account the 
                correlation between the covariate of the
                interest and other covariates. Some calculations also take 
                into account the competing risks and stratified analysis. 
                This package also includes
                a set of functions to calculate power and sample size
                for testing main effect in the survival analysis of 
                randomized clinical trials and conditional logistic regression for nested case-control study.
	"""
	
	cran = "powerSurvEpi" 

	version("0.1.3", md5="cfac294465abac111d314845e76b1fba")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
