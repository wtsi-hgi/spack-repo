# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmtmb(RPackage):
	"""Fit Hidden Markov Models using Template Model Builder

	Fitting hidden Markov models using automatic differentiation 
  and Laplace approximation, allowing for fast inference and flexible covariate
  effects (including random effects and smoothing splines) on model parameters.
  The package is described by Michelot (2022) <arXiv:2211.14139>.
	"""
	
	homepage = "https://github.com/TheoMichelot/hmmTMB"
	cran = "hmmTMB" 

	version("1.0.2", md5="9d81305e70dcc37015c03bb3f8cdf7bd")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tmbstan", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
