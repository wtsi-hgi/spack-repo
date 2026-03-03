# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbmsplitmerge(RPackage):
	"""Inference for a Generalised SBM with a Split Merge Sampler

	Inference in a Bayesian framework for a generalised stochastic block model. The generalised stochastic block model (SBM) can capture group structure in network data without requiring conjugate priors on the edge-states. Two sampling methods are provided to perform inference on edge parameters and block structure: a split-merge Markov chain Monte Carlo algorithm and a Dirichlet process sampler. Green, Richardson (2001) <doi:10.1111/1467-9469.00242>; Neal (2000) <doi:10.1080/10618600.2000.10474879>; Ludkin (2019) <arXiv:1909.09421>.
	"""
	
	cran = "SBMSplitMerge" 

	version("1.1.1", md5="5fd5730b442c651d114ffcda895c95d8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
