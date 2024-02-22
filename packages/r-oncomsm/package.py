# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncomsm(RPackage):
	"""Bayesian Multi-State Models for Early Oncology

	Implements methods to fit a parametric Bayesian multi-state model
    to tumor response data.
    The model can be used to sample from the predictive distribution to impute
    missing data and calculate probability of success for custom decision
    criteria in early clinical trials during an ongoing trial.
    The inference is implemented using 'stan'.
	"""
	
	homepage = "https://boehringer-ingelheim.github.io/oncomsm/"
	cran = "oncomsm" 

	version("0.1.4", md5="5a916725083277dde8c35ec04b18536b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppnumerical@0.4:", type=("build", "run"))
	depends_on("r-rstan@2.18:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
