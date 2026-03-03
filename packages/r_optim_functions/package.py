# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimFunctions(RPackage):
	"""Standard Benchmark Optimization Functions

	A set of standard benchmark optimization functions for R and
    a common interface to sample them.
	"""
	
	cran = "optim.functions" 

	version("0.1", md5="2c2f928d48041cb38a7622a63e2a2dca")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
