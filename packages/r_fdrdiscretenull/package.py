# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdrdiscretenull(RPackage):
	"""False Discovery Rate Procedures Under Discrete and Heterogeneous
Null Distributions

	It is known that current false discovery rate (FDR) procedures can be very conservative when applied to multiple testing in the discrete paradigm where p-values (and test statistics) have discrete and heterogeneous null distributions. This package implements more powerful weighted or adaptive FDR procedures for FDR control and estimation in the discrete paradigm. The package takes in the original data set rather than just the p-values in order to carry out the adjustments for discreteness and heterogeneity of p-value distributions. The package implements methods for two types of test statistics and their p-values: (a) binomial test on if two independent Poisson distributions have the same means, (b) Fisher's exact test on if the conditional distribution is the same as the marginal distribution for two binomial distributions, or on if two independent binomial distributions have the same probabilities of success.
	"""
	
	homepage = "http://math.wsu.edu/faculty/xchen/welcome.php"
	cran = "fdrDiscreteNull" 

	version("1.4", md5="aa60f46cb6bd921e0b0c8ce918000e70")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
