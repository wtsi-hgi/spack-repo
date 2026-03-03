# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmsc(RPackage):
	"""Hierarchical Model of Species Communities

	Hierarchical Modelling of Species Communities (HMSC) is
   a model-based approach for analyzing community ecological data. 
   This package implements it in the Bayesian framework with Gibbs
   Markov chain Monte Carlo (MCMC) sampling (Tikhonov et al. (2020)
   <doi:10.1111/2041-210X.13345>).
	"""
	
	homepage = "https://www.helsinki.fi/en/researchgroups/statistical-ecology/software/hmsc"
	cran = "Hmsc" 

	version("3.0-13", md5="151997665e209a466f49c16f825eec34")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bayeslogit", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
