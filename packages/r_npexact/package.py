# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpexact(RPackage):
	"""Exact Nonparametric Hypothesis Tests for the Mean, Variance and
Stochastic Inequality

	Provides several novel exact hypothesis tests with minimal assumptions on the errors. The tests are exact, meaning that their p-values are correct for the given sample sizes (the p-values are not derived from asymptotic analysis). The test for stochastic inequality is for ordinal comparisons based on two independent samples and requires no assumptions on the errors. The other tests include tests for the mean and variance of a single sample and comparing means in independent samples. All these tests only require that the data has known bounds (such as percentages that lie in [0,100]. These bounds are part of the input.
	"""
	
	homepage = "https://github.com/zauster/npExact"
	cran = "npExact" 

	version("0.2", md5="bfab660547f6d98c4d564f7c24388783")

	depends_on("r@3.2:", type=("build", "run"))
