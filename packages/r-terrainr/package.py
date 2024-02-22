# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTerrainr(RPackage):
	"""Landscape Visualizations in R and 'Unity'

	Functions for the retrieval, manipulation, and visualization
    of 'geospatial' data, with an aim towards producing '3D' landscape
    visualizations in the 'Unity' '3D' rendering engine. Functions are
    also provided for retrieving elevation data and base map tiles from
    the 'USGS' National Map <https://apps.nationalmap.gov/services/>.
	"""
	
	homepage = "https://docs.ropensci.org/terrainr/"
	cran = "terrainr" 

	version("0.7.5", md5="a0eb4b6bf8852e882a399bee63de4e56")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magick@2.5:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf@1.0.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-unifir", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
