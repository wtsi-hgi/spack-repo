# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQragadget(RPackage):
	"""A 'Shiny' Gadget for Interactive 'QRA' Visualizations

	Upload raster data and easily create interactive quantitative risk analysis 'QRA' visualizations. Select
    from numerous color palettes, base-maps, and different configurations.
	"""
	
	homepage = "https://github.com/paulgovan/qragadget"
	cran = "QRAGadget" 

	version("0.3.0", md5="fdbc1ab72546914d4289b0da85d878c2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
