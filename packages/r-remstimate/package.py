# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemstimate(RPackage):
	"""Optimization Frameworks for Tie-Oriented and Actor-Oriented
Relational Event Models

	A comprehensive set of tools designed for optimizing likelihood within a tie-oriented (Butts, C., 2008, <doi:10.1111/j.1467-9531.2008.00203.x>) or an actor-oriented modelling framework (Stadtfeld, C., & Block, P., 2017, <doi:10.15195/v4.a14>) in relational event networks. The package accommodates both frequentist and Bayesian approaches. The frequentist approaches that the package incorporates are the Maximum Likelihood Optimization (MLE) and the Gradient-based Optimization  (GDADAMAX). The Bayesian methodologies included in the package are the Bayesian Sampling Importance Resampling (BSIR) and the Hamiltonian Monte Carlo (HMC). The flexibility of choosing between frequentist and Bayesian optimization approaches allows researchers to select the estimation approach which aligns the most with their analytical preferences.
	"""
	
	homepage = "https://github.com/TilburgNetworkGroup/remstimate"
	cran = "remstimate" 

	version("2.3.8", md5="b0337e254c691b04e2811b4024207a0e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-remify", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-remstats@3.2.1:", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
