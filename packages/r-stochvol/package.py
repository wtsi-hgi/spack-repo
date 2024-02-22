# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStochvol(RPackage):
	"""Efficient Bayesian Inference for Stochastic Volatility (SV)
Models

	Efficient algorithms for fully Bayesian estimation of stochastic volatility (SV) models with and without asymmetry (leverage) via Markov chain Monte Carlo (MCMC) methods. Methodological details are given in Kastner and Frühwirth-Schnatter (2014) <doi:10.1016/j.csda.2013.01.002> and Hosszejni and Kastner (2019) <doi:10.1007/978-3-030-30611-3_8>; the most common use cases are described in Hosszejni and Kastner (2021) <doi:10.18637/jss.v100.i12> and Kastner (2016) <doi:10.18637/jss.v069.i05> and the package examples.
	"""
	
	homepage = "https://gregorkastner.github.io/stochvol/"
	cran = "stochvol" 

	version("3.2.3", md5="9f997f346557e0d905c65729f56146f3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda@0.19:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.900:", type=("build", "run"))
