# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdgebundler(RPackage):
	"""Circle Plot with Bundled Edges

	Generates interactive circle plots with the nodes around the
    circumference and linkages between the connected nodes using hierarchical
    edge bundling via the D3 JavaScript library. See <http://d3js.org/> for more
    information on D3.
	"""
	
	homepage = "https://github.com/garthtarr/edgebundleR"
	cran = "edgebundleR" 

	version("0.1.4", md5="a081820c7a1ba89958b356a9c6951385")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
