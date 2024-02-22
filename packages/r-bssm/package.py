# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBssm(RPackage):
	"""Bayesian Inference of Non-Linear and Non-Gaussian State Space
Models

	Efficient methods for Bayesian inference of state space models 
    via Markov chain Monte Carlo (MCMC) based on parallel 
    importance sampling type weighted estimators 
    (Vihola, Helske, and Franks, 2020, <doi:10.1111/sjos.12492>), 
    particle MCMC, and its delayed acceptance version. 
    Gaussian, Poisson, binomial, negative binomial, and Gamma
    observation densities and basic stochastic volatility models 
    with linear-Gaussian state dynamics, as well as general non-linear Gaussian 
    models and discretised diffusion models are supported. 
    See Helske and Vihola (2021, <doi:10.32614/RJ-2021-103>) for details.
	"""
	
	homepage = "https://github.com/helske/bssm"
	cran = "bssm" 

	version("2.0.2", md5="a1235d8be6cfbf742b99a6340863e8c6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-coda@0.18.1:", type=("build", "run"))
	depends_on("r-diagis", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ramcmc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-sitmo", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
