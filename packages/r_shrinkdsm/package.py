# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShrinkdsm(RPackage):
	"""Efficient Bayesian Inference for Dynamic Survival Models with
Shrinkage

	Efficient Markov chain Monte Carlo (MCMC) algorithms for fully 
    Bayesian estimation of dynamic survival models with shrinkage priors. 
    Details on the algorithms used are provided in Wagner (2011) <doi:10.1007/s11222-009-9164-5>, 
    Bitto and Frühwirth-Schnatter (2019) <doi:10.1016/j.jeconom.2018.11.006> and
    Cadonna et al. (2020) <doi:10.3390/econometrics8020020>.
	"""
	
	cran = "shrinkDSM" 

	version("0.2.0", md5="ca7d8dcf7a427af021e2238bb0e334ce")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stochvol", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-shrinktvp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
