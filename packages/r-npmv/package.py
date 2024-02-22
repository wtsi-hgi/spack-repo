# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpmv(RPackage):
	"""Nonparametric Comparison of Multivariate Samples

	Performs analysis of one-way multivariate data, for small samples using Nonparametric techniques. Using approximations for ANOVA Type, Wilks' Lambda, Lawley Hotelling, and Bartlett Nanda Pillai Test statics, the package compares the multivariate distributions for a single explanatory variable.  The comparison is also performed using a permutation test for each of the four test statistics. The package also performs an all-subsets algorithm regarding variables and regarding factor levels. 
	"""
	
	cran = "npmv" 

	version("2.4.0", md5="793e0f223c9198ba3958f385636990bb")

	depends_on("r-formula", type=("build", "run"))
