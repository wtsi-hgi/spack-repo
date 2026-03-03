# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatematrix(RPackage):
	"""Bayesian Estimation of the Evolutionary Rate Matrix

	The Evolutionary Rate Matrix is a variance-covariance matrix which describes both the rates of trait evolution and the evolutionary correlation among multiple traits. This package has functions to estimate these parameters using Bayesian MCMC. It is possible to test if the pattern of evolutionary correlations among traits has changed between predictive regimes painted along the branches of the phylogenetic tree. Regimes can be created a priori or estimated as part of the MCMC under a joint estimation approach. The package has functions to run MCMC chains, plot results, evaluate convergence, and summarize posterior distributions.
	"""
	
	homepage = "https://github.com/Caetanods/ratematrix"
	cran = "ratematrix" 

	version("1.2.4", md5="fe79ed22a488fe36463d6c8642ed6282")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-phylolm", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-mvmorph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
