# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNptest(RPackage):
	"""Nonparametric Bootstrap and Permutation Tests

	Robust nonparametric bootstrap and permutation tests for location, correlation, and regression problems, as described in Helwig (2019a) <doi:10.1002/wics.1457> and Helwig (2019b) <doi:10.1016/j.neuroimage.2019.116030>. Univariate and multivariate tests are supported. For each problem, exact tests and Monte Carlo approximations are available. Five different nonparametric bootstrap confidence intervals are implemented. Parallel computing is implemented via the 'parallel' package.
	"""
	
	cran = "nptest" 

	version("1.1", md5="3cd3c38a279e6afc5e2cdf51c88584bd")

