# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcodiet(RPackage):
	"""Estimating a Diet Matrix from Biotracer and Stomach Content Data

	Biotracers and stomach content analyses are combined in a Bayesian hierarchical model
    to estimate a probabilistic topology matrix (all trophic link probabilities) and a diet matrix 
    (all diet proportions).
    The package relies on the JAGS software and the 'jagsUI' package to run a Markov chain Monte Carlo 
    approximation of the different variables.
	"""
	
	homepage = "https://github.com/pyhernvann/EcoDiet"
	cran = "EcoDiet" 

	version("2.0.0", md5="5d1fa3236c5af9d1aae146a4c10f214f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-coda@0.19:", type=("build", "run"))
	depends_on("r-jagsui@1.5.2:", type=("build", "run"))
	depends_on("r-ggmcmc@1.1:", type=("build", "run"))
	depends_on("jags@4.3:", type=("build", "link", "run"))
