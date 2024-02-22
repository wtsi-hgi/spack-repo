# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovr(RPackage):
	"""Test Coverage for Packages.

	Track and report code coverage for your package and (optionally) upload the
	results to a coverage service like 'Codecov' <http://codecov.io> or
	'Coveralls' <https://coveralls.io/>. Code coverage is a measure of the
	amount of code being exercised by a set of tests. It is an indirect measure
	of test quality and completeness. This package is compatible with any
	testing methodology or framework and tracks coverage of both R code and
	compiled C/C++/FORTRAN code."""

	cran = "covr"

	version("3.6.4", md5="8fadf3538ed1edfefb3a20bd5c5e887d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-withr@1.0.2:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
