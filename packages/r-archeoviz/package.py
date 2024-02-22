# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcheoviz(RPackage):
	"""Visualisation, Exploration, and Web Communication of
Archaeological Spatial Data

	An R 'Shiny' application for the visualisation, interactive exploration, and web communication of archaeological spatial data. It includes interactive 3D and 2D visualisations, generation of cross sections and maps of the remains, and display an interactive timeline of the work made in a site. Simple spatial statistics can be performed (convex hull, regression surfaces, 2D kernel density estimation), as well as exporting data to other online applications for more complex methods. 'archeoViz' can be used locally or deployed on a server, either with interactive input of data or with a static data set. Example is provided at <https://analytics.huma-num.fr/archeoviz/en>.
	"""
	
	homepage = "https://archeoviz.hypotheses.org"
	cran = "archeoViz" 

	version("1.3.4", md5="78d72875e1673223846fadbba32c8764")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-cxhull", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
