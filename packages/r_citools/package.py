# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitools(RPackage):
	"""Confidence or Prediction Intervals, Quantiles, and Probabilities
for Statistical Models

	Functions to append confidence intervals, prediction intervals,
    and other quantities of interest to data frames. All appended quantities
    are for the response variable, after conditioning on the model and covariates.
    This package has a data frame first syntax that allows for easy piping.
    Currently supported models include (log-) linear, (log-) linear mixed,
    generalized linear models, generalized linear mixed models, and
    accelerated failure time models.
	"""
	
	homepage = "https://github.com/jthaman/ciTools"
	cran = "ciTools" 

	version("0.6.1", md5="a4b4dff3dd9b74e08982d2c0c37e4825")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
