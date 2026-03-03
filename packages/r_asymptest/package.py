# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsymptest(RPackage):
	"""A Simple R Package for Classical Parametric Statistical Tests
and Confidence Intervals in Large Samples

	One and two sample mean and variance
 tests (differences and ratios) are considered.
 The test statistics are all expressed in the same
 form as the Student t-test, which facilitates their
 presentation in the classroom. This contribution
 also fills the gap of a robust (to non-normality)
 alternative to the chi-square single variance test
 for large samples, since no such procedure is implemented
 in standard statistical software.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "asympTest" 

	version("0.1.4", md5="b98692bc1fe277cb62442d0aacac5d08")

	depends_on("r@1.8:", type=("build", "run"))
