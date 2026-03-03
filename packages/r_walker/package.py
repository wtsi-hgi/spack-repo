# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWalker(RPackage):
	"""Bayesian Generalized Linear Models with Time-Varying
Coefficients

	Efficient Bayesian generalized linear models with time-varying coefficients 
    as in Helske (2022, <doi:10.1016/j.softx.2022.101016>). Gaussian, Poisson, and binomial 
    observations are supported. The Markov chain Monte Carlo (MCMC) computations are done using 
    Hamiltonian Monte Carlo provided by Stan, using a state space representation 
    of the model in order to marginalise over the coefficients for efficient sampling. 
    For non-Gaussian models, the package uses the importance sampling type estimators based on 
    approximate marginal MCMC as in Vihola, Helske, Franks (2020, <doi:10.1111/sjos.12492>).
	"""
	
	homepage = "https://github.com/helske/walker"
	cran = "walker" 

	version("1.0.8", md5="118d2b651e9e0ee50fd6dd12ebafcb39")

	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12.9:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kfas", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
