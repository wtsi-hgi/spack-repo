# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvrm2perm(RPackage):
	"""Permutation Test for Comparing Restricted Mean Survival Time

	Performs the permutation test using difference in the restricted mean survival time (RMST) between groups as a summary measure of the survival time distribution. When the sample size is less than 50 per group, it has been shown that there is non-negligible inflation of the type I error rate in the commonly used asymptotic test for the RMST comparison. Generally, permutation tests can be useful in such a situation. However, when we apply the permutation test for the RMST comparison, particularly in small sample situations, there are some cases where the survival function in either group cannot be defined due to censoring in the permutation process. Horiguchi and Uno (2020) <doi:10.1002/sim.8565> have examined six workable solutions to handle this numerical issue. It performs permutation tests with implementation of the six methods outlined in the paper when the numerical issue arises during the permutation process. The result of the asymptotic test is also provided for a reference.
	"""
	
	cran = "survRM2perm" 

	version("0.1.0", md5="93417d9976689040f27d5a4b29ea8cdc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
