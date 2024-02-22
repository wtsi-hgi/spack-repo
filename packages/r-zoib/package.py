# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoib(RPackage):
	"""Bayesian Inference for Beta Regression and Zero-or-One Inflated
Beta Regression

	Fits beta regression and zero-or-one inflated beta regression and obtains Bayesian Inference of the model via the Markov Chain Monte Carlo approach implemented in JAGS.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "zoib" 

	version("1.6", md5="fd726958a45635bc567a234926434997")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
