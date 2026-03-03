# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstac(RPackage):
	"""Client Library for SpatioTemporal Asset Catalog

	Provides functions to access, search and download spacetime earth
    observation data via SpatioTemporal Asset Catalog (STAC). This package 
    supports the version 1.0.0 (and older) of the STAC specification
    (<https://github.com/radiantearth/stac-spec>). 
    For further details see Simoes et al. (2021) <doi:10.1109/IGARSS47720.2021.9553518>.
	"""
	
	homepage = "https://brazil-data-cube.github.io/rstac/"
	cran = "rstac" 

	version("1.0.0", md5="eee498037d2a63633ce5e9191cb327cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
