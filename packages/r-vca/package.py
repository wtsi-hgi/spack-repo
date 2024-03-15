# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVca(RPackage):
	"""Variance Component Analysis

	
 ANOVA and REML estimation of linear mixed models is implemented, once following
 Searle et al. (1991, ANOVA for unbalanced data), once making use of the 'lme4' package.
 The primary objective of this package is to perform a variance component analysis (VCA)
 according to CLSI EP05-A3 guideline "Evaluation of Precision of Quantitative Measurement
 Procedures" (2014). There are plotting methods for visualization of an experimental design,
 plotting random effects and residuals. For ANOVA type estimation two methods for computing
 ANOVA mean squares are implemented (SWEEP and quadratic forms). The covariance matrix of 
 variance components can be derived, which is used in estimating confidence intervals. Linear
 hypotheses of fixed effects and LS means can be computed. LS means can be computed at specific
 values of covariables and with custom weighting schemes for factor variables. See ?VCA for a
 more comprehensive description of the features. 
	"""
	
	cran = "VCA" 

	version("1.5.1", md5="8041fa126b398cc2176c8f51c608b6c1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
