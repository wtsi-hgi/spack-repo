# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapedit(RPackage):
	"""Interactive Editing of Spatial Data in R

	Suite of interactive functions and helpers for selecting and editing
    geospatial data.
	"""
	
	homepage = "https://github.com/r-spatial/mapedit"
	cran = "mapedit" 

	version("0.6.0", md5="73addd7e8c2f3c8130e6571b59225ad5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools@0.3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-leafem", type=("build", "run"))
	depends_on("r-leaflet@2.0.1:", type=("build", "run"))
	depends_on("r-leaflet-extras@1:", type=("build", "run"))
	depends_on("r-leafpm", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf@0.5.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
