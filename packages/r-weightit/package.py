# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightit(RPackage):
	"""Weighting for Covariate Balance in Observational Studies

	Generates balancing weights for causal effect estimation in observational studies with
             binary, multi-category, or continuous point or longitudinal treatments by easing and
             extending the functionality of several R packages and providing in-house estimation methods.
             Available methods include propensity score weighting using generalized linear models, gradient
             boosting machines, the covariate balancing propensity score algorithm, inverse probability tilting, Bayesian additive regression trees, and
             SuperLearner, and directly estimating balancing weights using entropy balancing, energy balancing, and optimization-based weights. Also
             allows for assessment of weights and checking of covariate balance by interfacing directly
             with the 'cobalt' package. See the vignette "Installing Supporting Packages" for instructions on how
             to install any package 'WeightIt' uses, including those that may not be on CRAN.
	"""
	
	homepage = "https://ngreifer.github.io/WeightIt/"
	cran = "WeightIt" 

	version("1.0.0", md5="f067e8735a88c80c239899cdc7a8b8c2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cobalt@4.5.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-chk@0.8.1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-backports@1.4.1:", type=("build", "run"))
