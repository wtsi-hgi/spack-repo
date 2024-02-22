# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmle(RPackage):
	"""Targeted Maximum Likelihood Estimation

	Targeted maximum likelihood estimation of point treatment effects (Targeted Maximum Likelihood Learning, The International Journal of Biostatistics, 2(1), 2006.  This version automatically estimates the additive treatment effect among the treated (ATT) and among the controls (ATC).  The tmle() function calculates the adjusted marginal difference in mean outcome associated with a binary point treatment, for continuous or binary outcomes.  Relative risk and odds ratio estimates are also reported for binary outcomes. Missingness in the outcome is allowed, but not in treatment assignment or baseline covariate values.  The population mean is calculated when there is missingness, and no variation in the treatment assignment. The tmleMSM() function estimates the parameters of a marginal structural model for a binary point treatment effect. Effect estimation stratified by a binary mediating variable is also available. An ID argument can be used to identify repeated measures. Default settings call 'SuperLearner' to estimate the Q and g portions of the likelihood, unless values or a user-supplied regression function are passed in as arguments. 
	"""
	
	homepage = "https://CRAN.R-project.org/package=tmle"
	cran = "tmle" 

	version("2.0.0", md5="f5c726036407fc3ad627ccba01d483ab")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-superlearner@2:", type=("build", "run"))
