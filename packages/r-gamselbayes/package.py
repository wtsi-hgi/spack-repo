# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamselbayes(RPackage):
	"""Bayesian Generalized Additive Model Selection

	Generalized additive model selection via approximate Bayesian inference is provided. Bayesian mixed model-based penalized splines with spike-and-slab-type coefficient prior distributions are used to facilitate fitting and selection. The approximate Bayesian inference engine options are: (1) Markov chain Monte Carlo and (2) mean field variational Bayes. Markov chain Monte Carlo has better Bayesian inferential accuracy, but requires a longer run-time. Mean field variational Bayes is faster, but less accurate. The methodology is described in He and Wand (2023) <arXiv:2201.00412>. 
	"""
	
	cran = "gamselBayes" 

	version("2.0-1", md5="f549b064752badd9f27aadfa123a0b1f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
