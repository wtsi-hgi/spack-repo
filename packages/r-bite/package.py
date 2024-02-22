# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBite(RPackage):
	"""Bayesian Integrative Models of Trait Evolution

	Contains the JIVE (joint inter and intra-specific model of variance evolution) model and other Bayesian models aimed at understanding trait evolution. The goal of the package is to join phylogenetic comparative models (PCM) that tend to integrate various type of data (individual observations, environmental data, fossil data) into a hierarchical Bayesian framework. It contains various PCMs as well as functions to join those models into a hierarchical Bayesian framework in a flexible and user friendly way. It contains various Markov chain Monte-Carlo (MCMC) algorithms, methods for model comparison and many plotting function for pre- and post-processing data visualization. Finally, this package integrates functions allowing bridges between 'R' and the 'BEAST2' implementations of PCMs. Kostikova A, Silvestro D, Pearman PB, Salamin N (2016) <doi:10.1093/sysbio/syw010>. Gaboriau T, Mendes FK, Joly S, Silvestro D, Salamin N (in prep).
	"""
	
	cran = "bite" 

	version("0.3", md5="f2f38cf30699f2a642e9e7d509f53245")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-vioplot", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
