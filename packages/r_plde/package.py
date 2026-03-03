# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlde(RPackage):
	"""Penalized Log-Density Estimation Using Legendre Polynomials

	We present a penalized log-density estimation method using Legendre polynomials with lasso penalty to adjust estimate's smoothness. Re-expressing the logarithm of the density estimator via a linear combination of Legendre polynomials, we can estimate parameters by maximizing the penalized log-likelihood function. Besides, we proposed an implementation strategy that builds on the coordinate decent algorithm, together with the Bayesian information criterion (BIC).
	"""
	
	cran = "plde" 

	version("0.1.2", md5="a1cdf18b97a055805241638ae8a53d48")

