# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComriskmodel(RPackage):
	"""Fitting of Complementary Risk Models

	Evaluates the probability density function (PDF), cumulative distribution function (CDF), quantile function (QF), random numbers and maximum likelihood estimates (MLEs) of well-known complementary binomial-G, complementary negative binomial-G and complementary geometric-G families of distributions taking baseline models such as exponential, extended exponential,  Weibull,  extended Weibull, Fisk, Lomax, Burr-XII and Burr-X. The functions also allow computing the goodness-of-fit measures namely the Akaike-information-criterion (AIC), the Bayesian-information-criterion (BIC), the minimum value of the negative log-likelihood (-2L) function, Anderson-Darling (A) test, Cramer-Von-Mises (W) test, Kolmogorov-Smirnov test, P-value and convergence status. Moreover, some commonly used data sets from the fields of actuarial, reliability, and medical science are also provided. Related works include: 
  a) Tahir, M. H., & Cordeiro, G. M. (2016). Compounding of distributions: a survey and new generalized classes. Journal of Statistical Distributions and Applications, 3, 1-35. 
  <doi:10.1186/s40488-016-0052-1>.  
	"""
	
	cran = "ComRiskModel" 

	version("0.2.0", md5="cc7536067486ebd192bb62fbbcfbca09")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-adequacymodel", type=("build", "run"))
