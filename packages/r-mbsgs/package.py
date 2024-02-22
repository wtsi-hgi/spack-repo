# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbsgs(RPackage):
	"""Multivariate Bayesian Sparse Group Selection with Spike and Slab

	An implementation of a Bayesian sparse group model using spike and slab priors in a regression context. It is designed for regression with a multivariate response variable, but also provides an implementation for univariate response.
	"""
	
	cran = "MBSGS" 

	version("1.1.0", md5="7b002fd7993e5b2c772364abdabc8ccd")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
