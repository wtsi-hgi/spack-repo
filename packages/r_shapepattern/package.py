# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapepattern(RPackage):
	"""Tools for Analyzing Shapes and Patterns

	This is an evolving and growing collection of tools for the quantification, assessment, and comparison of shape and pattern. This collection provides tools for: (1) the spatial decomposition of planar shapes using 'ShrinkShape' to incrementally shrink shapes to extinction while computing area, perimeter, and number of parts at each iteration of shrinking; the spectra of results are returned in graphic and tabular formats (Remmel 2015) <doi:10.1111/cag.12222>, (2) simulating landscape patterns, (3) provision of tools for estimating composition and configuration parameters from a categorical (binary) landscape map (grid) and then simulates a selected number of statistically similar landscapes. Class-focused pattern metrics are computed for each simulated map to produce empirical distributions against which statistical comparisons can be made. The code permits the analysis of single maps or pairs of maps (Remmel and Fortin 2013) <doi:10.1007/s10980-013-9905-x>, (4) counting the number of each first-order pattern element and converting that information into both frequency and empirical probability vectors (Remmel 2020) <doi:10.3390/e22040420>, and (5) computing the porosity of raster patches <doi:10.3390/su10103413>. NOTE: This is a consolidation of existing packages ('PatternClass', 'ShapePattern') to begin warehousing all shape and pattern code in a common package. Additional utility tools for handling data are provided and this package will be added to as more tools are created, cleaned-up, and documented.  Note that all future developments will appear in this package and that 'PatternClass' will eventually be archived.
	"""
	
	cran = "ShapePattern" 

	version("3.0.1", md5="9aad93dcc827069ec9bfe87fa496b986")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-landscapemetrics", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
