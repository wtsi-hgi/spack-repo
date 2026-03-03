# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtest(RPackage):
	"""Periodicity Tests in Short Time Series

	Implements p-value computations using an approximation to the cumulative distribution function for a variety of tests for periodicity. These tests include harmonic regression tests with normal and double exponential errors as well as modifications of Fisher's g test. An accompanying vignette illustrates the application of these tests.
	"""
	
	cran = "ptest" 

	version("1.0-8", md5="a34000c0fc6ca495f1e5a6b78764b854")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-quantreg@5:", type=("build", "run"))
