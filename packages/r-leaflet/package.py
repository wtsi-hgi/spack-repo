# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeaflet(RPackage):
	"""Create Interactive Web Maps with the JavaScript 'Leaflet' Library.

	Create and customize interactive maps using the 'Leaflet' JavaScript
	library and the 'htmlwidgets' package. These maps can be used directly from
	the R console, from 'RStudio', in Shiny apps and R Markdown documents."""

	cran = "leaflet"

	version("2.2.1", md5="798961353e12b0eeabff5de4e744a6e2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.4:", type=("build", "run"))
	depends_on("r-jquerylib", type=("build", "run"))
	depends_on("r-leaflet-providers@2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-raster@3.6.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
