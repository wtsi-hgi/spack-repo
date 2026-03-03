# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPec(RPackage):
	"""Prediction Error Curves for Risk Prediction Models in Survival
Analysis

	Validation of risk predictions obtained from survival models and
    competing risk models based on censored data using inverse weighting and
    cross-validation. Most of the 'pec' functionality has been moved to 'riskRegression'.
	"""
	
	cran = "pec" 

	version("2023.04.12", md5="72dd114007975159b146cc64f86ed820")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-prodlim@1.4.9:", type=("build", "run"))
	depends_on("r-foreach@1.4.2:", type=("build", "run"))
	depends_on("r-rms@4.2.0:", type=("build", "run"))
	depends_on("r-survival@2.37.7:", type=("build", "run"))
	depends_on("r-riskregression@2020.2.5:", type=("build", "run"))
	depends_on("r-lava@1.4.1:", type=("build", "run"))
	depends_on("r-timereg@1.8.9:", type=("build", "run"))
