# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTemporal(RPackage):
	"""Parametric Time to Event Analysis

	Performs maximum likelihood based estimation and inference on time to event data, possibly subject to non-informative right censoring. FitParaSurv() provides maximum likelihood estimates of model parameters and distributional characteristics, including the mean, median, variance, and restricted mean. CompParaSurv() compares the mean, median, and restricted mean survival experiences of two treatment groups. Candidate distributions include the exponential, gamma, generalized gamma, log-normal, and Weibull. 
	"""
	
	cran = "Temporal" 

	version("0.3.0.1", md5="59b4d280714a142a4bdc98cdff7d1649")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
