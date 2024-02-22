# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdfa(RPackage):
	"""Bayesian Dynamic Factor Analysis (DFA) with 'Stan'

	Implements Bayesian dynamic factor analysis with 'Stan'. Dynamic 
    factor analysis is a dimension reduction tool for multivariate time series.
    'bayesdfa' extends conventional dynamic factor models in several ways. 
    First, extreme events may be estimated in the latent trend by modeling
    process error with a student-t distribution. Second, alternative constraints
    (including proportions are allowed). Third, the estimated
    dynamic factors can be analyzed with hidden Markov models to evaluate
    support for latent regimes.
	"""
	
	homepage = "https://fate-ewi.github.io/bayesdfa/"
	cran = "bayesdfa" 

	version("1.3.2", md5="72bb6ea599e3bda53de3bc99a89af0fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-mgcv@1.8.13:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
