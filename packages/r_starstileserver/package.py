# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarstileserver(RPackage):
	"""A Dynamic Tile Server for R

	Makes it possible to serve map tiles for web maps (e.g. leaflet) based on a function or a stars object without having to render them in advance. This enables parallelization of the rendering, separating the data source and visualization location and to provide web services.
	"""
	
	homepage = "https://bartk.gitlab.io/starsTileServer"
	cran = "starsTileServer" 

	version("0.1.1", md5="614415646e9dbe81947f89707665744e")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-plumber", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
