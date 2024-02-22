# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoxut(RPackage):
	"""Document Unit Tests Roxygen-Style

	Much as 'roxygen2' allows one to document functions in the same file as the function itself, 'roxut'  allows one to write the unit tests in the same file as the function.  Once processed, the unit tests are moved to the appropriate directory.  Currently supports 'testthat' and 'tinytest' frameworks. The 'roxygen2' package provides much of the infrastructure.
	"""
	
	homepage = "https://github.com/bryanhanson/roxut"
	cran = "roxut" 

	version("0.4.0", md5="8808a4c811f51d81c523fa9608c25369")

	depends_on("r-roxygen2@7.1:", type=("build", "run"))
