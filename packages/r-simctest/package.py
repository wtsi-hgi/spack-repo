# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimctest(RPackage):
	"""Safe Implementation of Monte Carlo Tests

	Algorithms for the implementation and evaluation of Monte Carlo tests, as well as for their use in multiple testing procedures.
	"""
	
	homepage = "http://www2.imperial.ac.uk/~agandy"
	cran = "simctest" 

	version("2.6", md5="74d08cf7356ca7ed585930db3d808c15")

	depends_on("r@2.2:", type=("build", "run"))
