# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazamalocationutils(RPackage):
	"""Manage Spatial Metadata for Known Locations

	Utility functions for discovering and managing metadata 
    associated with spatially unique "known locations". Applications include
    all fields of environmental monitoring (e.g. air and water quality) where 
    data are collected at stationary sites.
	"""
	
	homepage = "https://github.com/MazamaScience/MazamaLocationUtils"
	cran = "MazamaLocationUtils" 

	version("0.4.3", md5="3ff5ce4402c5d724578b842160c34d7d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geodist@0.0.8:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mazamacoreutils@0.5.1:", type=("build", "run"))
	depends_on("r-mazamaspatialutils@0.8.6:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidygeocoder", type=("build", "run"))
