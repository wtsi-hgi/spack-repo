# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistanceto(RPackage):
	"""Calculate Distance to Features

	Calculates distances from point locations to features.
    The usual approach for eg. resource selection function analyses is to
    generate a complete distance to features surface then sample it with your 
    observed and random points. Since these raster based approaches can be
    pretty costly with large areas, and often lead to memory issues in R, 
    the distanceto package opts to compute these distances using
    efficient, vector based approaches. As a helper, there's a decidedly 
    low-res raster based approach for visually inspecting your region's 
    distance surface. But the workhorse is distance_to.
	"""
	
	homepage = "https://github.com/robitalec/distance-to"
	cran = "distanceto" 

	version("0.0.3", md5="b03d74c681e441cf53f0f9b53e2254d6")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
