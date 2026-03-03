# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonotonicity(RPackage):
	"""Test for Monotonicity in Expected Asset Returns, Sorted by
Portfolios

	Test for monotonicity in financial variables sorted by portfolios. It is conventional practice in empirical research to form portfolios of assets ranked by a certain sort variable. A t-test is then used to consider the mean return spread between the portfolios with the highest and lowest values of the sort variable. Yet comparing only the average returns on the top and bottom portfolios does not provide a sufficient way to test for a monotonic relation between expected returns and the sort variable. This package provides nonparametric tests for the full set of monotonic patterns by Patton, A. and Timmermann, A. (2010) <doi:10.1016/j.jfineco.2010.06.006> and compares the proposed results with extant alternatives such as t-tests, Bonferroni bounds, and multivariate inequality tests through empirical applications and simulations.
	"""
	
	homepage = "https://github.com/skoestlmeier/monotonicity"
	cran = "monotonicity" 

	version("1.3.1", md5="7a93e4ba27355324d44692e73ff915a5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
