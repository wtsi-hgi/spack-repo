# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesct(RPackage):
	"""Simulation and Analysis of Adaptive Bayesian Clinical Trials

	Simulation and analysis of Bayesian adaptive clinical trials for binomial, Gaussian, and time-to-event data types, 
      incorporates historical data and allows early stopping for futility or early success. The package uses novel 
      and efficient Monte Carlo methods for estimating Bayesian posterior probabilities, evaluation of loss to follow up, 
      and imputation of incomplete data. The package has the functionality for dynamically incorporating historical data 
      into the analysis via the power prior or non-informative priors.
	"""
	
	homepage = "https://github.com/thevaachandereng/bayesCT/"
	cran = "bayesCT" 

	version("0.99.3", md5="c659650bb52e09a49656ae29d4c30257")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bayesdp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
