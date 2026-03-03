# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayestools(RPackage):
	"""Tools for Bayesian Analyses

	Provides tools for conducting Bayesian analyses and Bayesian model averaging 
    (Kass and Raftery, 1995, <doi:10.1080/01621459.1995.10476572>, 
    Hoeting et al., 1999, <doi:10.1214/ss/1009212519>). The package contains 
    functions for creating a wide range of prior distribution objects, mixing posterior 
    samples from 'JAGS' and 'Stan' models, plotting posterior distributions, and etc...
    The tools for working with prior distribution span from visualization, generating 'JAGS' 
    and 'bridgesampling' syntax to basic functions such as rng, quantile, and distribution functions. 
	"""
	
	homepage = "https://fbartos.github.io/BayesTools/"
	cran = "BayesTools" 

	version("0.2.17", md5="edd4604a7e42a6d5b3bc113474a7ce7f")

	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-bridgesampling", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
