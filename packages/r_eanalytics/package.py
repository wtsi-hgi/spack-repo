# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REanalytics(RPackage):
	"""Dynamic Web-Based Analytics for the Energy Industry

	A 'Shiny' web application for energy industry analytics.
      Take an overview of the industry, measure Key Performance Indicators,
      identify changes in the industry over time, and discover new relationships in the data.
	"""
	
	homepage = "https://github.com/paulgovan/eanalytics"
	cran = "eAnalytics" 

	version("0.3", md5="dc5c7421102b5eadf87d87e91a7b80f5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-energyr", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-plotly@4.5.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
