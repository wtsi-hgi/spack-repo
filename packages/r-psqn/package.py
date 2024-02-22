# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsqn(RPackage):
	"""Partially Separable Quasi-Newton

	Provides quasi-Newton methods to minimize partially separable
    functions. The methods are largely described by  
    Nocedal and Wright (2006) <doi:10.1007/978-0-387-40065-5>.
	"""
	
	homepage = "https://github.com/boennecd/psqn"
	cran = "psqn" 

	version("0.3.1", md5="696c0cf9c266eb547cff9b238f90a081")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
