# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrailtymmpen(RPackage):
	"""Efficient Algorithm for High-Dimensional Frailty Model

	The penalized and non-penalized Minorize-Maximization (MM) method for frailty models to fit the clustered data, multi-event data and recurrent data. Least absolute shrinkage and selection operator (LASSO), minimax concave penalty (MCP) and smoothly clipped absolute deviation (SCAD) penalized functions are implemented. All the methods are computationally efficient. These general methods are proposed based on the following papers,
    Huang, Xu and Zhou (2022) <doi:10.3390/math10040538>,
    Huang, Xu and Zhou (2023) <doi:10.1177/09622802221133554>.
	"""
	
	cran = "frailtyMMpen" 

	version("1.2.1", md5="a87c1f3e376a2f4d8c8e6ffdb1c4d33d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
