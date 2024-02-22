# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypercube(RPackage):
	"""Organizing Data in Hypercubes

	Provides functions and methods for organizing data in hypercubes
  (i.e., a multi-dimensional cube). Cubes are generated from molten data frames.
  Each cube can be manipulated with five operations: rotation (change.dimensionOrder()),
  dicing and slicing (add.selection(), remove.selection()), drilling down (add.aggregation()),
  and rolling up (remove.aggregation()).
	"""
	
	cran = "hypercube" 

	version("0.2.1", md5="843ce82c31dc71bb4d06c9afa77f18e5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
