# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianvars(RPackage):
	"""MCMC Estimation of Bayesian Vectorautoregressions

	Efficient Markov Chain Monte Carlo (MCMC) algorithms for the
    fully Bayesian estimation of vectorautoregressions (VARs) featuring
    stochastic volatility (SV). Implements state-of-the-art shrinkage
    priors following Gruber & Kastner (2023) <arXiv:2206.04902>.
    Efficient equation-per-equation estimation following Kastner & Huber
    (2020) <doi:10.1002/for.2680> and Carrerio et al. (2021)
    <doi:10.1016/j.jeconom.2021.11.010>.
	"""
	
	homepage = "https://github.com/luisgruber/bayesianVARs"
	cran = "bayesianVARs" 

	version("0.1.2", md5="8e43852f951f93a42541c93a9d1d2717")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-factorstochvol", type=("build", "run"))
	depends_on("r-gigrvg@0.7:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stochvol", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
