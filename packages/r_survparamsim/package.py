# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvparamsim(RPackage):
	"""Parametric Survival Simulation with Parameter Uncertainty

	Perform survival simulation with parametric survival model generated from 'survreg' function in 'survival' package.
    In each simulation coefficients are resampled from variance-covariance matrix of parameter estimates to 
    capture uncertainty in model parameters.
    Prediction intervals of Kaplan-Meier estimates and hazard ratio of treatment effect can be further calculated using simulated survival data.
	"""
	
	homepage = "https://github.com/yoshidk6/survParamSim"
	cran = "survParamSim" 

	version("0.1.6", md5="ba3c3690f1fa4d45274f30b7faeff821")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survival@2.43:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
