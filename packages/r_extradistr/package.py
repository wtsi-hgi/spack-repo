# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtradistr(RPackage):
	"""Additional Univariate and Multivariate Distributions

	Density, distribution function, quantile function
    and random generation for a number of univariate
    and multivariate distributions. This package implements the
    following distributions: Bernoulli, beta-binomial, beta-negative
    binomial, beta prime, Bhattacharjee, Birnbaum-Saunders,
    bivariate normal, bivariate Poisson, categorical, Dirichlet,
    Dirichlet-multinomial, discrete gamma, discrete Laplace,
    discrete normal, discrete uniform, discrete Weibull, Frechet,
    gamma-Poisson, generalized extreme value, Gompertz,
    generalized Pareto, Gumbel, half-Cauchy, half-normal, half-t,
    Huber density, inverse chi-squared, inverse-gamma, Kumaraswamy,
    Laplace, location-scale t, logarithmic, Lomax, multivariate
    hypergeometric, multinomial, negative hypergeometric,
    non-standard beta, normal mixture, Poisson mixture, Pareto,
    power, reparametrized beta, Rayleigh, shifted Gompertz, Skellam,
    slash, triangular, truncated binomial, truncated normal,
    truncated Poisson, Tukey lambda, Wald, zero-inflated binomial,
    zero-inflated negative binomial, zero-inflated Poisson.
	"""
	
	homepage = "https://github.com/twolodzko/extraDistr"
	cran = "extraDistr" 

	version("1.10.0", md5="8d92a34b8fd30ac9b0191b2ab8300b66")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
