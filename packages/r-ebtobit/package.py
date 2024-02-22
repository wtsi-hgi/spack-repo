# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbtobit(RPackage):
	"""Empirical Bayesian Tobit Matrix Estimation

	Estimation tools for multidimensional Gaussian means using
    empirical Bayesian g-modeling. Methods are able to handle fully observed data as
    well as left-, right-, and interval-censored observations (Tobit
    likelihood); descriptions of these methods can be found in Barbehenn and
    Zhao (2023) <arXiv:2306.07239>. Additional, lower-level functionality based
    on Kiefer and Wolfowitz (1956) <doi:10.1214/aoms/1177728066> and Jiang and
    Zhang (2009) <doi:10.1214/08-AOS638> is provided that can be used to
    accelerate many empirical Bayes and nonparametric maximum likelihood
    problems.
	"""
	
	homepage = "https://github.com/barbehenna/ebTobit"
	cran = "ebTobit" 

	version("1.0.1", md5="5a413bdf99964afeea40a4158bd8c6d0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
