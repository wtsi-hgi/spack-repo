# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUhm(RPackage):
	"""Unified Zero-Inflated Hurdle Regression Models

	Run a Gibbs sampler for hurdle models to analyze data showing an excess of zeros, which is common in zero-inflated count and semi-continuous models. The package includes the hurdle model under Gaussian, Gamma, inverse Gaussian, Weibull, Exponential, Beta, Poisson, negative binomial, logarithmic, Bell, generalized Poisson, and binomial distributional assumptions. The models described in Ganjali et al. (2024).
	"""
	
	homepage = "https://github.com/tbaghfalaki/UHM"
	cran = "UHM" 

	version("0.3.0", md5="b8b45e4fd1cce30feaef50071bb0aa9f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jagsui", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("jags@4:", type=("build", "link", "run"))
