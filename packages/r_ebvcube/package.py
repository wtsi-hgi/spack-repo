# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbvcube(RPackage):
	"""Working with netCDF for Essential Biodiversity Variables

	The concept of Essential Biodiversity Variables (EBV, <https://geobon.org/ebvs/what-are-ebvs/>) 
    comes with a data structure based on the Network Common Data Form (netCDF). 
    The 'ebvcube' 'R' package provides functionality to easily create, access and 
    visualise this data. The EBV netCDFs can be downloaded from the EBV Data 
    Portal: Christian Langer/ iDiv (2020) <https://portal.geobon.org/>. 
	"""
	
	homepage = "https://github.com/LuiseQuoss/ebvcube"
	cran = "ebvcube" 

	version("0.1.7", md5="298292dd39aa089f6fdbbb87229b88a0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memuse", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-ncmeta", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyterra", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("gdal", type=("build", "link", "run"))
