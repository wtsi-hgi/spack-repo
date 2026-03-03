# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REwgof(RPackage):
	"""Goodness-of-Fit Tests for the Exponential and Two-Parameter
Weibull Distributions

	Contains a large number of the goodness-of-fit tests for the Exponential and Weibull distributions classified into families: the tests based on the empirical distribution function, the tests based on the probability plot, the tests based on the normalized spacings, the tests based on the Laplace transform and the likelihood based tests.
	"""
	
	cran = "EWGoF" 

	version("2.2.2", md5="d41e87b9410f367a3706726eb5b1177a")

	depends_on("r-rcpp", type=("build", "run"))
