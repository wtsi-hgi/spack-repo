# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBang(RPackage):
	"""Bayesian Analysis, No Gibbs

	Provides functions for the Bayesian analysis of some simple 
    commonly-used models, without using Markov Chain Monte Carlo (MCMC) 
    methods such as Gibbs sampling.  The 'rust' package
    <https://cran.r-project.org/package=rust> is used to simulate a random 
    sample from the required posterior distribution, using the generalized 
    ratio-of-uniforms method.  See Wakefield, Gelfand and Smith (1991) 
    <DOI:10.1007/BF01889987> for details. At the moment three conjugate 
    hierarchical models are available: beta-binomial, gamma-Poisson and a 1-way 
    analysis of variance (ANOVA).
	"""
	
	homepage = "https://paulnorthrop.github.io/bang/"
	cran = "bang" 

	version("1.0.3", md5="86900b854a26de53f860930f86fee266")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bayesplot@1.1:", type=("build", "run"))
	depends_on("r-rust@1.2.2:", type=("build", "run"))
