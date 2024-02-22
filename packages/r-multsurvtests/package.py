# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultsurvtests(RPackage):
	"""Permutation Tests for Multivariate Survival Analysis

	Multivariate version of the two-sample Gehan and logrank tests, as described in L.J Wei & J.M Lachin (1984) and Persson et al. (2019).
	"""
	
	homepage = "https://github.com/lukketotte/MultSurvTests"
	cran = "MultSurvTests" 

	version("0.2", md5="ccc60322b391077ec39ce8babe0a843c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
