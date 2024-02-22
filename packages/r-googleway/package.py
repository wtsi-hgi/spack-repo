# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogleway(RPackage):
	"""Accesses Google Maps APIs to Retrieve Data and Plot Maps

	Provides a mechanism to plot a 'Google Map' from 'R' and overlay
    it with shapes and markers. Also provides access to 'Google Maps' APIs,
    including places, directions, roads, distances, geocoding, elevation and
    timezone.
	"""
	
	cran = "googleway" 

	version("2.7.8", md5="d811ef0770f944526f7d5d4a2ca72a2a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.20:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-jqr", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-googlepolylines@0.7.1:", type=("build", "run"))
