# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxaipw(RPackage):
	"""Doubly Robust Inference for Cox Marginal Structural Model with
Informative Censoring

	Doubly robust estimation and inference of log hazard ratio under the Cox marginal structural model with informative censoring. An augmented inverse probability weighted estimator that involves 3 working models, one for conditional failure time T, one for conditional censoring time C and one for propensity score. Both models for T and C can depend on both a binary treatment A and additional baseline covariates Z, while the propensity score model only depends on Z. With the help of cross-fitting techniques, achieves the rate-doubly robust property that allows the use of most machine learning or non-parametric methods for all 3 working models, which are not permitted in classic inverse probability weighting or doubly robust estimators. When the proportional hazard assumption is violated, CoxAIPW estimates a causal estimated that is a weighted average of the time-varying log hazard ratio. Reference: Luo, J. (2023). Statistical Robustness - Distributed Linear Regression, Informative Censoring, Causal Inference, and Non-Proportional Hazards [Unpublished doctoral dissertation]. University of California San Diego.; Luo & Xu (2022) <doi:10.48550/arXiv.2206.02296>; Rava (2021) <https://escholarship.org/uc/item/8h1846gs>.
	"""
	
	homepage = "https://github.com/charlesluo1002/CoxAIPW"
	cran = "CoxAIPW" 

	version("0.0.3", md5="37d52475db05ed11886f298062e073c6")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
	depends_on("r-polspline", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
