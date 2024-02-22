# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestfit(RPackage):
	"""Statistical Modelling for Plant Size Distributions

	Developed for the following tasks. 1 ) Computing the probability density function,
             cumulative distribution function, random generation, and estimating the parameters
 			 of the eleven mixture models. 2 ) Point estimation of the parameters of two - 
			 parameter Weibull distribution using twelve methods and three - parameter Weibull 
			 distribution using nine methods. 3 ) The Bayesian inference for the three - 
			 parameter Weibull distribution. 4 ) Estimating parameters of the three - parameter
			 Birnbaum - Saunders, generalized exponential, and Weibull distributions fitted to
			 grouped data using three methods including approximated maximum likelihood, 
			 expectation maximization, and maximum likelihood. 5 ) Estimating the parameters
			 of the gamma, log-normal, and Weibull mixture models fitted to the grouped data
			 through the EM algorithm, 6 ) Estimating parameters of the nonlinear height curve
			 fitted to the height - diameter observation, 7 ) Estimating parameters, computing
			 probability density function, cumulative distribution function, and generating
			 realizations from gamma shape mixture model introduced by Venturini et al. (2008)
			 <doi:10.1214/07-AOAS156> , 8 ) The Bayesian inference, computing probability
			 density function, cumulative distribution function, and generating realizations
			 from four-parameter Johnson SB distribution, 9 ) Robust multiple linear regression
			 analysis when error term follows skewed t distribution, 10 ) Estimating 
			 parameters of a given distribution fitted to grouped data using method of maximum
			 likelihood, and 11 ) Estimating parameters of the Johnson SB distribution through 
			 the Bayesian, method of moment, conditional maximum likelihood, and two - percentile 
			 method.
	"""
	
	cran = "ForestFit" 

	version("2.2.3", md5="95bf26fc9c465c29728e1febe71bd85d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ars", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
