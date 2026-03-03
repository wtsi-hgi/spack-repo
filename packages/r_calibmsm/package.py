# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibmsm(RPackage):
	"""Calibration Plots for the Transition Probabilities from
Multistate Models

	Assess the calibration of an existing (i.e. previously developed) multistate
  model through calibration plots. 
  Calibration is assessed using one of three methods. 1) Calibration methods for 
  binary logistic regression models applied at a fixed time point in conjunction 
  with inverse probability of censoring weights. 2) Calibration methods for 
  multinomial logistic regression models applied at a fixed time point in conjunction 
  with inverse probability of censoring weights. 3) Pseudo-values estimated using 
  the Aalen-Johansen estimator of observed risk. All methods are applied in conjunction
  with landmarking when required. These calibration plots evaluate the calibration 
  (in a validation cohort of interest) of the transition probabilities estimated from an 
  existing multistate model. While package development has focused on multistate 
  models, calibration plots can be produced for any model which utilises information 
  post baseline to update predictions (e.g. dynamic models); competing risks models; 
  or standard single outcome survival models, where predictions can be made at 
  any landmark time. The underpinning methodology is currently undergoing peer review; see Pate et al. (2023) <arXiv:2308.13394>
  and Pate et al. (2023) <https://alexpate30.github.io/calibmsm/articles/Overview.html>.
	"""
	
	homepage = "https://alexpate30.github.io/calibmsm/"
	cran = "calibmsm" 

	version("1.0.0", md5="0636a6679521b7eccb9595cfd95d55ff")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mstate", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
