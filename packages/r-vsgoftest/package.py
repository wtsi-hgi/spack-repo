# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsgoftest(RPackage):
	"""Goodness-of-Fit Tests Based on Kullback-Leibler Divergence

	An implementation of Vasicek and Song goodness-of-fit tests. Several functions are provided to estimate differential Shannon entropy, i.e., estimate Shannon entropy of real random variables with density, and test the goodness-of-fit of some family of distributions, including uniform, Gaussian, log-normal, exponential, gamma, Weibull, Pareto, Fisher, Laplace and beta distributions; see Lequesne and Regnault (2020) <doi:10.18637/jss.v096.c01>.
	"""
	
	cran = "vsgoftest" 

	version("1.0-1", md5="49c795cbfbdaf125f66e0e01566824b0")

	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
