# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMerlin(RPackage):
	"""Mixed Effects Regression for Linear, Non-Linear and User-Defined
Models

	Fits linear, non-linear, and user-defined mixed effects regression models following 
  the framework developed by Crowther (2017) <arXiv:1710.02223>. 'merlin' can fit multivariate 
  outcome models of any type, each of which could be repeatedly measured (longitudinal), with 
  any number of levels, and with any number of random effects at each level. Standard 
  distributions/models available include the Bernoulli, Gaussian, Poisson, beta, 
  negative-binomial, and time-to-event/survival models include the exponential, 
  Gompertz, Royston-Parmar, Weibull and general hazard model. 'merlin' provides a 
  flexible predictor syntax, allowing the user to define variables, random effects, 
  spline and fractional polynomial functions, functions of 
  other outcome models, and any interaction between each of them. Non-linear and 
  time-dependent effects are seamlessly incorporated into the predictor. 'merlin' 
  allows multivariate normal random effects, which are integrated out using Gaussian 
  quadrature or Monte-Carlo integration. Note, 'merlin' is based on the 'Stata' package 
  of the same name, described in Crowther (2018) <arXiv:1806.01615>.
	"""
	
	homepage = "https://www.mjcrowther.co.uk/software/merlin"
	cran = "merlin" 

	version("0.1.0", md5="94630a0659fa887be25162f3b7c348dc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
