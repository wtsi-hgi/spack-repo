# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmcalibration(RPackage):
	"""Calibration Curves for Clinical Prediction Models

	Fit calibrations curves for clinical prediction models and calculate several associated 
  metrics (Eavg, E50, E90, Emax). Ideally predicted probabilities from a prediction model 
  should align with observed probabilities. Calibration curves relate predicted probabilities 
  (or a transformation thereof) to observed outcomes via a flexible non-linear smoothing function. 
  'pmcalibration' allows users to choose between several smoothers (regression splines, generalized 
  additive models/GAMs, lowess, loess). Both binary and time-to-event outcomes are supported. 
  See Van Calster et al. (2016) <doi:10.1016/j.jclinepi.2015.12.005>; 
  Austin and Steyerberg (2019) <doi:10.1002/sim.8281>; 
  Austin et al. (2020) <doi:10.1002/sim.8570>.
	"""
	
	homepage = "https://github.com/stephenrho/pmcalibration"
	cran = "pmcalibration" 

	version("0.1.0", md5="99c3f9f367ddaf8cf71cc1ea3fe89357")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
