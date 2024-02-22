# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamtx(RPackage):
	"""Sensitivity Assessment to Unmeasured Confounding with Multiple
Treatments

	A sensitivity analysis approach for unmeasured confounding in observational data with multiple treatments and a binary outcome. This approach derives the general bias formula and provides adjusted causal effect estimates in response to various assumptions about the degree of unmeasured confounding. Nested multiple imputation is embedded within the Bayesian framework to integrate   uncertainty about the sensitivity parameters and sampling variability.  Bayesian Additive Regression Model (BART) is used for outcome modeling. The causal estimands are the conditional average treatment effects (CATE) based on the risk difference.  For more details, see paper: Hu L et al. (2020) A flexible sensitivity analysis approach for unmeasured confounding with multiple treatments and a binary outcome with application to SEER-Medicare lung cancer data <arXiv:2012.06093>. 
	"""
	
	cran = "SAMTx" 

	version("0.3.0", md5="e789bd0d9bc64dec73d486c27619c9b6")

	depends_on("r-bart", type=("build", "run"))
