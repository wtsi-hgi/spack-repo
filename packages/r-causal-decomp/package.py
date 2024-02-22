# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalDecomp(RPackage):
	"""Causal Decomposition Analysis

	We implement causal decomposition analysis using the methods proposed by Park, Lee, and Qin (2020) and Park, Kang, and Lee (2021+) <arXiv:2109.06940>. This package allows researchers to use the multiple-mediator-imputation, single-mediator-imputation, and product-of-coefficients regression methods to estimate the initial disparity, disparity reduction, and disparity remaining. It also allows to make the inference conditional on baseline covariates. We also implement sensitivity analysis for the causal decomposition analysis using R-squared values as sensitivity parameters (Park, Kang, Lee, and Ma, 2023).
	"""
	
	cran = "causal.decomp" 

	version("0.1.0", md5="3cb783d114628a222dce8caf4df19a3a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-cbps", type=("build", "run"))
	depends_on("r-psweight", type=("build", "run"))
	depends_on("r-spelling", type=("build", "run"))
