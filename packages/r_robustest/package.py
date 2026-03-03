# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustest(RPackage):
	"""Calibrated Correlation and Two-Sample Tests

	Implementation of corrected two-sample tests. A corrected version of the Pearson and Kendall correlation tests, 
 the Mann-Whitney (Wilcoxon) rank sum test, the Wilcoxon signed rank test and a variance test are implemented.
 The package also proposes a test for the median and an independence test between two continuous variables of Kolmogorov-Smirnov's type. 
 All these corrected tests are asymptotically calibrated in the sense that the probability of rejection under the null hypothesis is 
 asymptotically equal to the level of the test. See <arXiv:2211.08784> for more details on the statistical tests.
	"""
	
	cran = "robusTest" 

	version("1.0.1", md5="78526dfd6afce3e777375d2ee5c652a6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
