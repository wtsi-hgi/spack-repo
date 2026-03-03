# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeaflegend(RPackage):
	"""Add Custom Legends to 'leaflet' Maps

	Provides extensions to the 'leaflet' package to 
    customize legends with images, text styling, orientation, sizing,
    and symbology and functions to create symbols to plot on maps.
	"""
	
	homepage = "https://leaflegend.roh.engineering"
	cran = "leaflegend" 

	version("1.2.0", md5="d6164c2669ab5624d75802609c871191")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
