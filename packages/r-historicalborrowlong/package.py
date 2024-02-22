# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistoricalborrowlong(RPackage):
	"""Longitudinal Bayesian Historical Borrowing Models

	Historical borrowing in clinical trials can improve
  precision and operating characteristics. This package supports
  a longitudinal hierarchical model to borrow historical
  control data from other studies to better characterize the
  control response of the current study. It also quantifies
  the amount of borrowing through longitudinal benchmark models (independent
  and pooled). The hierarchical model approach to historical borrowing
  is discussed by Viele et al. (2013) <doi:10.1002/pst.1589>.
	"""
	
	homepage = "https://wlandau.github.io/historicalborrowlong/"
	cran = "historicalborrowlong" 

	version("0.0.8", md5="818746ebdb6aea033c478ec5e586eae6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-clustermq", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-trialr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
