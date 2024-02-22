# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlippymath(RPackage):
	"""Slippy Map Tile Tools

	Provides functions for performing common tasks when working with
  slippy map tile service APIs e.g. Google maps, Open Street Map, Mapbox, Stamen,
  among others. Functionality includes converting from latitude and longitude to
  tile numbers, determining tile bounding boxes, and compositing tiles to a
  georeferenced raster image.
	"""
	
	homepage = "https://www.github.com/milesmcbain/slippymath"
	cran = "slippymath" 

	version("0.3.1", md5="365bbf2ac6ed08c05084bae8a7c7dc2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
