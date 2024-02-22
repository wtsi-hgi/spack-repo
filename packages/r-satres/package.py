# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSatres(RPackage):
	"""Grouping Satellite Bands by Spectral and Spatial Resolution

	Given raster files directly downloaded from various websites,
    it generates a raster structure where it merges them if they are tiles
    of the same scene and classifies them according to their spectral and
    spatial resolution for easy access by name.
	"""
	
	homepage = "https://josesamos.github.io/satres/"
	cran = "satres" 

	version("1.1.1", md5="30281c9a7985c8052aaf467ed6bcd414")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
