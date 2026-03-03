# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchr(RPackage):
	"""High Precise Measurement of R Expressions Execution Time

	Provides infrastructure to accurately measure and compare
    the execution time of R expressions.
	"""
	
	homepage = "https://gitlab.com/artemklevtsov/benchr"
	cran = "benchr" 

	version("0.2.5", md5="23947580c472a089c3aaa359f7809f31")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
