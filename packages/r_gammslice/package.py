# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGammslice(RPackage):
	"""Generalized Additive Mixed Model Analysis via Slice Sampling

	Uses a slice sampling-based Markov chain Monte Carlo to
        conduct Bayesian fitting and inference for generalized additive
        mixed models.  Generalized linear mixed models and generalized 
        additive models are also handled as special cases of generalized
        additive mixed models. The methodology and software is described 
        in Pham, T.H. and Wand, M.P. (2018). Australian and New Zealand
        Journal of Statistics, 60, 279-330 <DOI:10.1111/ANZS.12241>.
	"""
	
	cran = "gammSlice" 

	version("2.0-2", md5="ca339a7e330e22f3fccc59b15eb76ebf")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
