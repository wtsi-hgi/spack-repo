# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFutureTests(RPackage):
	"""Test Suite for 'Future API' Backends

	Backends implementing the 'Future' API, as defined by the 'future' package, should use the tests provided by this package to validate that they meet the minimal requirements of the 'Future' API.  The tests can be performed easily from within R or from outside of R from the command line making it straightforward to include them in package tests and in Continuous Integration (CI) pipelines.
	"""
	
	homepage = "https://future.tests.futureverse.org"
	cran = "future.tests" 

	version("0.7.0", md5="a7a260d0d31add8324093014de108b8d")

	depends_on("r-future@1.22.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
