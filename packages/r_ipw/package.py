# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpw(RPackage):
	"""Estimate Inverse Probability Weights

	Functions to estimate the probability to receive the observed treatment, based on
    individual characteristics. The inverse of these probabilities can be used as weights when
	estimating causal effects from observational data via marginal structural models. Both point
	treatment situations and longitudinal studies can be analysed. The same functions can be used to
	correct for informative censoring.	
	"""
	
	cran = "ipw" 

	version("1.2.1", md5="52e857ebdaa9837f7ff149af9549feab")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
