# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDunnTest(RPackage):
	"""Dunn's Test of Multiple Comparisons Using Rank Sums

	Computes Dunn's test (1964) for stochastic dominance and reports the results among multiple pairwise comparisons after a Kruskal-Wallis test for stochastic dominance among k groups (Kruskal and Wallis, 1952). The interpretation of stochastic dominance requires an assumption that the CDF of one group does not cross the CDF of the other. 'dunn.test' makes k(k-1)/2 multiple pairwise comparisons based on Dunn's z-test-statistic approximations to the actual rank statistics. The null hypothesis for each pairwise comparison is that the probability of observing a randomly selected value from the first group that is larger than a randomly selected value from the second group equals one half; this null hypothesis corresponds to that of the Wilcoxon-Mann-Whitney rank-sum test. Like the rank-sum test, if the data can be assumed to be continuous, and the distributions are assumed identical except for a difference in location, Dunn's test may be understood as a test for median difference. 'dunn.test' accounts for tied ranks.
	"""
	
	cran = "dunn.test" 

	version("1.3.5", md5="766dd9c2342ce7efadad6da433cbec14")

