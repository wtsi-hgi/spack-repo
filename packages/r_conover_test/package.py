# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConoverTest(RPackage):
	"""Conover-Iman Test of Multiple Comparisons Using Rank Sums

	Computes the Conover-Iman test (1979) for stochastic dominance and reports the results among multiple pairwise comparisons after a Kruskal-Wallis test for stochastic dominance among k groups (Kruskal and Wallis, 1952). The interpretation of stochastic dominance requires an assumption that the CDF of one group does not cross the CDF of the other. conover.test makes k(k-1)/2 multiple pairwise comparisons based on Conover-Iman t-test-statistic of the rank differences. The null hypothesis for each pairwise comparison is that the probability of observing a randomly selected value from the first group that is larger than a randomly selected value from the second group equals one half; this null hypothesis corresponds to that of the Wilcoxon-Mann-Whitney rank-sum test. Like the rank-sum test, if the data can be assumed to be continuous, and the distributions are assumed identical except for a difference in location, Conover-Iman test may be understood as a test for median difference. conover.test accounts for tied ranks. The Conover-Iman test is strictly valid if and only if the corresponding Kruskal-Wallis null hypothesis is rejected.
	"""
	
	cran = "conover.test" 

	version("1.1.5", md5="5ffa6bec2a2aa6cf5a59ea94f236f543")

