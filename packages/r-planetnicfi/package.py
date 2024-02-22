# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanetnicfi(RPackage):
	"""Processing of the 'Planet NICFI' Satellite Imagery

	It includes functions to download and process the 'Planet NICFI' (Norway's International Climate and Forest Initiative) Satellite Imagery utilizing the Planet Mosaics API <https://developers.planet.com/docs/basemaps/reference/#tag/Basemaps-and-Mosaics>. 'GDAL' (library for raster and vector geospatial data formats) and 'aria2c' (paralleled download utility) must be installed and configured in the user's Operating System.
	"""
	
	homepage = "https://github.com/mlampros/PlanetNICFI"
	cran = "PlanetNICFI" 

	version("1.0.5", md5="e878cd8c31fa0e8b692030e179ce1344")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("aria2", type=("build", "link", "run"))
	depends_on("gdal", type=("build", "link", "run"))
