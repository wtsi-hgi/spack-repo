# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmuoutlier(RPackage):
	"""Permutation Tests for Nonparametric Statistics

	Performs a permutation test on the difference between two location parameters, a permutation correlation test, a permutation F-test, the Siegel-Tukey test, a ratio mean deviance test.  Also performs some graphing techniques, such as for confidence intervals, vector addition, and Fourier analysis; and includes functions related to the Laplace (double exponential) and triangular distributions.  Performs power calculations for the binomial test.
	"""
	
	cran = "jmuOutlier" 

	version("2.2", md5="1f92d60478f62fd8a90d7059f4d8a8af")

	depends_on("r@2:", type=("build", "run"))
