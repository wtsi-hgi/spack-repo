# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvntest(RPackage):
	"""Goodness of Fit Tests for Multivariate Normality

	Routines for assessing multivariate normality. Implements three Wald's type chi-squared tests; non-parametric Anderson-Darling and Cramer-von Mises tests; Doornik-Hansen test,  Royston test and Henze-Zirkler test.
	"""
	
	cran = "mvnTest" 

	version("1.1-0", md5="0509c5244c6fcb140c5957938d02a93e")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
