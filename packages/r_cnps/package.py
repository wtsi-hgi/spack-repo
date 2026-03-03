# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnps(RPackage):
	"""Nonparametric Statistics

	We unify various nonparametric hypothesis testing problems in a framework of permutation testing, enabling hypothesis testing on multi-sample, multidimensional data and contingency tables. Most of the functions available in the R environment to implement permutation tests are single functions constructed for specific test problems; to facilitate the use of the package, the package encapsulates similar tests in a categorized manner, greatly improving ease of use.
    We will all provide functions for self-selected permutation scoring methods and self-selected p-value calculation methods (asymptotic, exact, and sampling). For two-sample tests, we will provide mean tests and estimate drift sizes; we will provide tests on variance; we will provide paired-sample tests; we will provide correlation coefficient tests under three measures. For multi-sample problems, we will provide both ordinary and ordered alternative test problems. For multidimensional data, we will implement multivariate means (including ordered alternatives) and multivariate pairwise tests based on four statistics; the components with significant differences are also calculated. For contingency tables, we will perform permutation chi-square test or ordered alternative.
	"""
	
	cran = "CNPS" 

	version("1.0.0", md5="deac071a9387e3a296481d041e6d09ee")

