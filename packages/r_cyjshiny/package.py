# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyjshiny(RPackage):
	"""Cytoscape.js Shiny Widget (cyjShiny)

	Wraps cytoscape.js as a shiny widget. cytoscape.js <https://js.cytoscape.org/> is a Javascript-based graph theory (network) library for visualization and analysis. This package supports the visualization of networks with custom visual styles and several available layouts. Demo Shiny applications are provided in the package code.  
	"""
	
	cran = "cyjShiny" 

	version("1.0.42", md5="794b00c136c44db050a142fb72a1d5ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
