# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoft(RPackage):
	"""Tests of Fit for some Probability Distributions

	Goodness-of-fit tests for skew-normal, gamma, inverse Gaussian, log-normal, 'Weibull', 'Frechet', Gumbel, normal, multivariate normal, Cauchy, Laplace or double exponential, exponential and generalized Pareto distributions. Parameter estimators for gamma, inverse Gaussian and generalized Pareto distributions.
	"""
	
	cran = "goft" 

	version("1.3.6", md5="32f18fc018a5f1807d1644a904aa6d22")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
