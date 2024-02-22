# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApproxot(RPackage):
	"""Approximate and Exact Optimal Transport Methods

	R and C++ functions to perform exact and 
  approximate optimal transport. All C++ methods can be linked 
  to other R packages via their header files. 
	"""
	
	homepage = "https://github.com/ericdunipace/approxOT"
	cran = "approxOT" 

	version("1.1.1", md5="0538af4fac10d4158a7906d8d20c5e92")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppcgal", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
