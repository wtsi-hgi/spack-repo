# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROceanis(RPackage):
	"""Cartography for Statistical Analysis

	Creating maps for statistical analysis such as proportional circles, choropleth, typology and flows. Some functions use 'shiny' or 'leaflet' technologies for dynamism and interactivity.
	The great features are :
	- Create maps in a web environment where the parameters are modifiable on the fly ('shiny' and 'leaflet' technologies).
	- Create interactive maps through zoom and pop-up ('leaflet' technology).
	- Create frozen maps with the possibility to add labels.
	"""
	
	homepage = "https://github.com/insee-psar-at/oceanis-package/"
	cran = "oceanis" 

	version("1.8.5", md5="ce8e242b04f44de299a4569f731e2eed")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny@1.4.0.2:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-classint@0.4.2:", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))
	depends_on("r-shinyjs@1.1:", type=("build", "run"))
	depends_on("r-shinythemes@1.1.2:", type=("build", "run"))
	depends_on("r-dt@0.12:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-leaflet@2.0.3:", type=("build", "run"))
	depends_on("r-leaflet-extras@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-lwgeom@0.2.1:", type=("build", "run"))
	depends_on("r-zip@2.1.1:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.4:", type=("build", "run"))
	depends_on("r-webshot@0.5.2:", type=("build", "run"))
