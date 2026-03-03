# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMps(RPackage):
	"""Estimating Through the Maximum Product Spacing Approach

	Developed for computing the probability density function, computing the cumulative distribution function, computing the quantile function, random generation, drawing q-q plot, and estimating the parameters of 24 G-family of statistical distributions via the maximum product spacing approach introduced in <https://www.jstor.org/stable/2345411>. The set of families contains: beta G distribution, beta exponential G distribution, beta extended G distribution, exponentiated G distribution, exponentiated exponential Poisson G distribution, exponentiated generalized G distribution, exponentiated Kumaraswamy G distribution, gamma type I G distribution, gamma type II G distribution, gamma uniform G distribution, gamma-X generated of log-logistic family of G distribution, gamma-X family of modified beta exponential G distribution, geometric exponential Poisson G distribution, generalized beta G distribution, generalized transmuted G distribution, Kumaraswamy G distribution, log gamma type I G distribution, log gamma type II G distribution, Marshall Olkin G distribution, Marshall Olkin Kumaraswamy G distribution, modified beta G distribution, odd log-logistic G distribution, truncated-exponential skew-symmetric G distribution, and Weibull G distribution.
	"""
	
	cran = "MPS" 

	version("2.3.1", md5="780236c3afb0af13a072a298aa910434")

	depends_on("r@3.1:", type=("build", "run"))
