# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestthatmulti(RPackage):
	"""Testing for R Packages with Multiple Attempts for Noisy Tests

	Runs tests using the 'testthat' package but allows for multiple
    attempts for a single test. This is useful for noisy or flaky tests
    that generally pass but can fail due to occasional random errors,
    such as numeric instability or using random data.
	"""
	
	cran = "testthatmulti" 

	version("0.1.0", md5="2e27bbd540c38ddeea109291e3db9966")

