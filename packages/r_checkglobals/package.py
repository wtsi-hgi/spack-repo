# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckglobals(RPackage):
	"""Static Analysis of R-Code Dependencies

	A minimal R-package to approximately detect global and imported functions or variables from R-source code or R-packages by static code analysis.
	"""
	
	homepage = "https://jorischau.github.io/checkglobals/"
	cran = "checkglobals" 

	version("0.1.0", md5="653bde510d424da738bf5166babb52b6")

	depends_on("r@4.1:", type=("build", "run"))
