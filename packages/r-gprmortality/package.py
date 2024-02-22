# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGprmortality(RPackage):
	"""Gaussian Process Regression for Mortality Rates

	A Bayesian statistical model for estimating child (under-five age group) and adult (15-60 age group) mortality.  The main challenge is how to combine and integrate these different time series and how to produce unified estimates of mortality rates during a specified time span. GPR is a Bayesian statistical model for estimating child and adult mortality rates which its data likelihood is mortality rates from different data sources such as: Death Registration System, Censuses or surveys. There are also various hyper-parameters for completeness of DRS, mean, covariance functions and variances as priors. This function produces estimations and uncertainty (95% or any desirable percentiles) based on sampling and non-sampling errors due to variation in data sources. The GP model utilizes Bayesian inference to update predicted mortality rates as a posterior in Bayes rule by combining data and a prior probability distribution over parameters in mean, covariance function, and the regression model. This package uses Markov Chain Monte Carlo (MCMC) to sample from posterior probability distribution by 'rstan' package in R. Details are given in Wang H, Dwyer-Lindgren L, Lofgren KT, et al. (2012) <doi:10.1016/S0140-6736(12)61719-X>, Wang H, Liddell CA, Coates MM, et al. (2014) <doi:10.1016/S0140-6736(14)60497-9> and Mohammadi, Parsaeian, Mehdipour et al. (2017) <doi:10.1016/S2214-109X(17)30105-5>.
	"""
	
	cran = "GPRMortality" 

	version("0.1.0", md5="c62a9af312f390ef42e07e4d48ebbf41")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
