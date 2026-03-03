# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoronoitreemap(RPackage):
	"""Voronoi Treemaps with Added Interactivity by Shiny

	The d3.js framework with the plugins d3-voronoi-map, d3-voronoi-treemap and d3-weighted-voronoi
        are used to generate Voronoi treemaps in R and in a shiny application.
        The computation of the Voronoi treemaps are based on Nocaj and Brandes (2012)
        <doi:10.1111/j.1467-8659.2012.03078.x>.
	"""
	
	homepage = "https://github.com/uRosConf/voronoiTreemap"
	cran = "voronoiTreemap" 

	version("0.2.0", md5="5e5307f468d6bd42fc07988d39c9042f")

	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
