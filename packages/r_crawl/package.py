# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrawl(RPackage):
	"""Fit Continuous-Time Correlated Random Walk Models to Animal
Movement Data

	Fit continuous-time correlated random walk models with time indexed
    covariates to animal telemetry data. The model is fit using the Kalman-filter on
    a state space version of the continuous-time stochastic movement process.
	"""
	
	cran = "crawl" 

	version("2.3.0", md5="19cd342913d1869fcf1e6b224c1bb9be")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
