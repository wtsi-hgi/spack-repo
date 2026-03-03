# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapdeck(RPackage):
	"""Interactive Maps Using 'Mapbox GL JS' and 'Deck.gl'

	Provides a mechanism to plot an interactive map using 'Mapbox GL' 
		(<https://docs.mapbox.com/mapbox-gl-js/api/>), a javascript library for interactive maps,
		and 'Deck.gl' (<https://deck.gl/>), a javascript library which uses 'WebGL' for 
		visualising large data sets.
	"""
	
	homepage = "https://symbolixau.github.io/mapdeck/articles/mapdeck.html"
	cran = "mapdeck" 

	version("0.3.5", md5="8ff9c1d37f04b0f506d8045a91f0e1bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-colourvalues@0.3.9:", type=("build", "run"))
	depends_on("r-googlepolylines@0.7.2:", type=("build", "run"))
	depends_on("r-geojsonsf@2.0.3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonify@1.2.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sfheaders@0.4.4:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-geometries@0.2.4:", type=("build", "run"))
	depends_on("r-interleave@0.1.2:", type=("build", "run"))
	depends_on("r-rapidjsonr", type=("build", "run"))
	depends_on("r-spatialwidget@0.2.5:", type=("build", "run"))
