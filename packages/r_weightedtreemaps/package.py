# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedtreemaps(RPackage):
	"""Generate and Plot Voronoi or Sunburst Treemaps from Hierarchical
Data

	Treemaps are a visually appealing graphical representation of
    numerical data using a space-filling approach. A plane or 'map' is
    subdivided into smaller areas called cells.  The cells in the map are
    scaled according to an underlying metric which allows to grasp the
    hierarchical organization and relative importance of many objects at
    once. This package contains two different implementations of treemaps,
    Voronoi treemaps and Sunburst treemaps.  The Voronoi treemap function
    subdivides the plot area in polygonal cells according to the highest
    hierarchical level, then continues to subdivide those parental cells
    on the next lower hierarchical level, and so on. The Sunburst treemap
    is a computationally less demanding treemap that does not require
    iterative refinement, but simply generates circle sectors that are
    sized according to predefined weights.  The Voronoi tesselation is
    based on functions from Paul Murrell (2012)
    <https://www.stat.auckland.ac.nz/~paul/Reports/VoronoiTreemap/voronoiTreeMap.html>.
	"""
	
	homepage = "https://github.com/m-jahn/WeightedTreemaps"
	cran = "WeightedTreemaps" 

	version("0.1.2", md5="b15465c349a0c546e9a7ef7457da02ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppcgal", type=("build", "run"))
