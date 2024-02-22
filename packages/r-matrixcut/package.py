# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixcut(RPackage):
	"""Determines Clustering Threshold Based on Similarity Values

	The user must supply a matrix filled with similarity values. The software will search for significant differences between similarity values at different hierarchical levels. The algorithm will return a Loess-smoothed plot of the similarity values along with the inflection point, if there are any. There is the option to search for an inflection point within a specified range. The package also has a function that will return the matrix components at a specified cutoff. References: Mullner. <ArXiv:1109.2378>; Cserhati, Carter. (2020, Journal of Creation 34(3):41-50), <https://dl0.creation.com/articles/p137/c13759/j34-3_64-73.pdf>.
	"""
	
	cran = "matrixcut" 

	version("0.0.1", md5="9da367a4e9611548a37841033c697a27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-inflection", type=("build", "run"))
