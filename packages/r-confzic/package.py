# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfzic(RPackage):
	"""Confidence Envelopes for Model Selection Criteria Based on
Minimum ZIC

	Narrow down the number of models to look at in model selection using the confidence envelopes based on the minimum ZIC (Generalized Information Criteria) values for regression and time series data. Functions involve the computation of multivariate normal-probabilities with covariance matrices based on minimum ZIC inverting the CDF of the minimum ZIC. It involves both the computation of singular and non-singular probabilities as described in Genz (1992) <[https:doi.org/10.2307/1390838]https:doi.org/10.2307/1390838>.
	"""
	
	cran = "ConfZIC" 

	version("1.0.1", md5="01de22568fbe3b069905a7e357a144ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cmna", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tidytable", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
