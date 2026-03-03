# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitbitviz(RPackage):
	"""'Fitbit' Visualizations

	Connection to the 'Fitbit' Web API <https://dev.fitbit.com/build/reference/web-api/> by including 'ggplot2' Visualizations, 'Leaflet' and 3-dimensional 'Rayshader' Maps. The 3-dimensional 'Rayshader' Map requires the installation of the 'CopernicusDEM' R package which includes the 30- and 90-meter elevation data.
	"""
	
	homepage = "https://github.com/mlampros/fitbitViz"
	cran = "fitbitViz" 

	version("1.0.6", md5="14edeedca1084137dc3ffd72a169632d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-varian", type=("build", "run"))
	depends_on("r-paletteer", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-leafgl", type=("build", "run"))
	depends_on("r-raster@3.6.3:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rayshader", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
