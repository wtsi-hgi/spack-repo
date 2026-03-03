# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCego(RPackage):
	"""Combinatorial Efficient Global Optimization

	Model building, surrogate model
    based optimization and Efficient Global Optimization in combinatorial
    or mixed search spaces.
	"""
	
	cran = "CEGO" 

	version("2.4.3", md5="163796ac0c9e308d2c40952748896b44")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-paramhelpers", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-anticlust", type=("build", "run"))
