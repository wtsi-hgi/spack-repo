# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatest(RPackage):
	"""Randomization Tests

	A collection of randomization tests, data sets and examples. The current version focuses on five testing problems and their implementation in empirical work. First, it facilitates the empirical researcher to test for particular hypotheses, such as comparisons of means, medians, and variances from k populations using robust permutation tests, which asymptotic validity holds under very weak assumptions, while retaining the exact rejection probability in finite samples when the underlying distributions are identical. Second, the description and implementation of a permutation test for testing the continuity assumption of the baseline covariates in the sharp regression discontinuity design (RDD) as in Canay and Kamat (2018) <https://goo.gl/UZFqt7>. More specifically, it allows the user to select a set of covariates and test the aforementioned hypothesis using a permutation test based on the Cramer-von Misses test statistic. Graphical inspection of the empirical CDF and histograms for the variables of interest is also supported in the package. Third, it provides the practitioner with an effortless implementation of a permutation test based on the martingale decomposition of the empirical process for testing for heterogeneous treatment effects in the presence of an estimated nuisance parameter as in Chung and Olivares (2021) <doi:10.1016/j.jeconom.2020.09.015>. Fourth, this version considers the two-sample goodness-of-fit testing problem under covariate adaptive randomization and implements a permutation test based on a prepivoted Kolmogorov-Smirnov test statistic. Lastly, it implements an asymptotically valid permutation test based on the quantile process for the hypothesis of constant quantile treatment effects in the presence of an estimated nuisance parameter.
	"""
	
	cran = "RATest" 

	version("0.1.10", md5="9930c9f4f088b97bbe4e849aba2c513f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
