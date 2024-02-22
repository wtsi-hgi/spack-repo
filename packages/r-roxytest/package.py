# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoxytest(RPackage):
	"""Various Tests with 'roxygen2'

	Various tests as 'roxygen2' roclets: e.g. 'testthat' and 'tinytest' tests. 
  Also other static analysis tools as checking parameter documentation consistency and others.
	"""
	
	cran = "roxytest" 

	version("0.0.2", md5="25e964c75c708e75551d8abe588ba046")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
