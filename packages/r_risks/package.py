# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRisks(RPackage):
	"""Estimate Risk Ratios and Risk Differences using Regression

	Risk ratios and risk differences are estimated using regression 
  models that allow for binary, categorical, and continuous exposures and 
  confounders. Implemented are marginal standardization after fitting logistic 
  models (g-computation) with delta-method and bootstrap standard errors, 
  Miettinen's case-duplication approach (Schouten et al. 1993, 
  <doi:10.1002/sim.4780121808>), log-binomial (Poisson) models with empirical 
  variance (Zou 2004, <doi:10.1093/aje/kwh090>), binomial models with starting 
  values from Poisson models (Spiegelman and Hertzmark 2005, 
  <doi:10.1093/aje/kwi188>), and others.
	"""
	
	homepage = "https://stopsack.github.io/risks/"
	cran = "risks" 

	version("0.4.2", md5="9244e078140f2dd7f61e1109442b879d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-bcaboot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
