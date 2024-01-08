# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RDensestbayes(RPackage):
	"""Density Estimation via Bayesian Inference Engines

	Bayesian density estimates for univariate continuous random samples are provided using the Bayesian inference engine paradigm. The engine options are: Hamiltonian Monte Carlo, the no U-turn sampler, semiparametric mean field variational Bayes and slice sampling. The methodology is described in Wand and Yu (2020) <arXiv:2009.06182>.
	"""
	
	cran = "densEstBayes" 

	version("1.0-2.2", md5="d9bacbd697be98f3907429dcee5e969d")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-stanheaders", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))

