# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivitycalibration(RPackage):
	"""A Calibrated Sensitivity Analysis for Matched Observational
Studies

	Implements the calibrated sensitivity analysis approach for matched observational studies. Our sensitivity analysis framework views matched sets as drawn from a super-population. The unmeasured confounder is modeled as a random variable. We combine matching and model-based covariate-adjustment methods to estimate the treatment effect. The hypothesized unmeasured confounder enters the picture as a missing covariate. We adopt a state-of-art Expectation Maximization (EM) algorithm to handle this missing covariate problem in generalized linear models (GLMs). As our method also estimates the effect of each observed covariate on the outcome and treatment assignment, we are able to calibrate the unmeasured confounder to observed covariates.
      Zhang, B., Small, D. S. (2018). <arXiv:1812.00215>.
	"""
	
	cran = "sensitivityCalibration" 

	version("0.0.1", md5="523071f07dcb8b53ab0a84ef7c004edb")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-relaimpo", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
