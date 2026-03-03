# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMovecost(RPackage):
	"""Calculation of Slope-Dependant Accumulated Cost Surface,
Least-Cost Paths, Least-Cost Corridors, Least-Cost Networks
Related to Human Movement Across the Landscape

	Provides the facility to calculate non-isotropic accumulated cost surface, least-cost paths, least-cost corridors, least-cost networks using a number of human-movement-related cost functions that can be selected by the user. It just requires a Digital Terrain Model, a start location and (optionally) destination locations. See Alberti (2019) <doi:10.1016/j.softx.2019.100331>.
	"""
	
	cran = "movecost" 

	version("2.1", md5="da41ca144cc982053952df7dcc829710")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-chron@2.3.56:", type=("build", "run"))
	depends_on("r-gdistance@1.2.2:", type=("build", "run"))
	depends_on("r-elevatr@0.3.4:", type=("build", "run"))
	depends_on("r-matrix@1.5:", type=("build", "run"))
	depends_on("r-raster@2.8.4:", type=("build", "run"))
	depends_on("r-sf@1.0.9:", type=("build", "run"))
	depends_on("r-sp@1.4:", type=("build", "run"))
	depends_on("r-terra@1.3:", type=("build", "run"))
