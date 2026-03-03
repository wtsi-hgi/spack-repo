# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootlr(RPackage):
	"""Bootstrapped Confidence Intervals for (Negative) Likelihood
Ratio Tests

	Computes appropriate confidence intervals for the likelihood ratio tests commonly used in medicine/epidemiology, using the method of Marill et al. (2015) <doi:10.1177/0962280215592907>.  It is particularly useful when the sensitivity or specificity in the sample is 100%.  Note that this does not perform the test on nested models--for that, see 'epicalc::lrtest'.
	"""
	
	cran = "bootLR" 

	version("1.0.2", md5="ce780d8356aa3b75218ef1e789019e67")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
