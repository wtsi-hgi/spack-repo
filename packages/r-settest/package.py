# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSettest(RPackage):
	"""Group Testing Procedures for Signal Detection and
Goodness-of-Fit

	It provides cumulative distribution function (CDF),
    quantile, p-value, statistical power calculator and random number generator
    for a collection of group-testing procedures, including the Higher Criticism
    tests, the one-sided Kolmogorov-Smirnov tests, the one-sided Berk-Jones tests,
    the one-sided phi-divergence tests, etc. The input are a group of p-values.
    The null hypothesis is that they are i.i.d. Uniform(0,1). In the context of
    signal detection, the null hypothesis means no signals. In the context of the
    goodness-of-fit testing, which contrasts a group of i.i.d. random variables to
    a given continuous distribution, the input p-values can be obtained by the CDF
    transformation. The null hypothesis means that these random variables follow the
    given distribution. For reference, see Hong Zhang, Jiashun Jin and Zheyang Wu. 
    "Distributions and Statistical Power of Optimal Signal-Detection Methods In Finite Cases",
    submitted.
	"""
	
	cran = "SetTest" 

	version("0.2.0", md5="0ccf38517ce6270b2e510f081913c39f")

