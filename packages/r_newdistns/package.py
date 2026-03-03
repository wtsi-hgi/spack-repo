# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewdistns(RPackage):
	"""Computes Pdf, Cdf, Quantile and Random Numbers, Measures of
Inference for 19 General Families of Distributions

	Computes the probability density function, cumulative distribution function, quantile function, random numbers and measures of inference for the following general families of  distributions (each family defined in terms of an arbitrary cdf G): Marshall Olkin G distributions, exponentiated G distributions, beta G distributions, gamma G distributions, Kumaraswamy G distributions, generalized beta G distributions, beta extended G distributions, gamma G distributions, gamma uniform G distributions, beta exponential G distributions, Weibull G distributions, log gamma G I distributions, log gamma G II distributions, exponentiated generalized G distributions, exponentiated Kumaraswamy G distributions, geometric exponential Poisson G distributions, truncated-exponential skew-symmetric G distributions, modified beta G distributions, and exponentiated exponential Poisson G distributions.
	"""
	
	cran = "Newdistns" 

	version("2.1", md5="0d990e31bfa7d5b63f0731739dad022a")

	depends_on("r-adequacymodel", type=("build", "run"))
