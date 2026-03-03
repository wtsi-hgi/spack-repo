# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdwreg(RPackage):
	"""Bayesian Inference for Discrete Weibull Regression

	A Bayesian regression model for discrete response, where the conditional distribution is modelled via a discrete Weibull distribution. This package provides an implementation of Metropolis-Hastings and Reversible-Jumps algorithms to draw samples from the posterior. It covers a wide range of regularizations through any two parameter prior. Examples are Laplace (Lasso), Gaussian (ridge), Uniform, Cauchy and customized priors like a mixture of priors. An extensive visual toolbox is included to check the validity of the results as well as several measures of goodness-of-fit.
	"""
	
	cran = "BDWreg" 

	version("1.3.0", md5="753331b072510bfef4cf4c62d7baf6b2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dwreg", type=("build", "run"))
