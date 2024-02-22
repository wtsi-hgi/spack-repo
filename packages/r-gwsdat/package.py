# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwsdat(RPackage):
	"""GroundWater Spatiotemporal Data Analysis Tool (GWSDAT)

	Shiny application for the analysis of groundwater
    monitoring data, designed to work with simple time-series data for
    solute concentration and ground water elevation, but can also plot
    non-aqueous phase liquid (NAPL) thickness if required. Also provides
    the import of a site basemap in GIS shapefile format.
	"""
	
	cran = "GWSDAT" 

	version("3.2.0", md5="a7552eb165db1969abb30a8447047079")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-officer@0.3.8:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
