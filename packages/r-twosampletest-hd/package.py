# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwosampletestHd(RPackage):
	"""A Two-Sample Test for the Equality of Distributions for
High-Dimensional Data

	For high-dimensional data whose main feature is a large number, p, of variables but a small sample size, the null hypothesis that the marginal distributions of p variables are the same for two groups is tested. We propose a test statistic motivated by the simple idea of comparing, for each of the p variables, the empirical characteristic functions computed from the two samples. If one rejects this global null hypothesis of no differences in distributions between the two groups, a set of permutation p-values is reported to identify which variables are not equally distributed in both groups.
	"""
	
	cran = "TwoSampleTest.HD" 

	version("1.2", md5="3eaec005326bff9d08f1f0c7fc5139ba")

	depends_on("r@3.5:", type=("build", "run"))
