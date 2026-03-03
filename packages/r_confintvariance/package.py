# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfintvariance(RPackage):
	"""Confidence Interval for the Univariate Population Variance
without Normality Assumption

	Surrounds the usual sample variance of a univariate numeric sample with a confidence interval for the population variance. This has been done so far only under the assumption that the underlying distribution is normal. Under the hood, this package implements the unique least-variance unbiased estimator of the variance of the sample variance, in a formula that is equivalent to estimating kurtosis and square of the population variance in an unbiased way and combining them according to the classical formula into an estimator of the variance of the sample variance. Both the sample variance and the estimator of its variance are U-statistics. By the theory of U-statistic, the resulting estimator is unique. See Fuchs, Krautenbacher (2016) <doi:10.1080/15598608.2016.1158675> and the references therein for an overview of unbiased estimation of variances of U-statistics.
	"""
	
	cran = "ConfIntVariance" 

	version("1.0.2", md5="9c92748bb0e4743570d628964cd19e31")

