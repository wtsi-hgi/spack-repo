# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTchazards(RPackage):
	"""Tropical Cyclone (Hurricane, Typhoon) Spatial Hazard Modelling

	Methods for generating modelled parametric Tropical Cyclone (TC) spatial hazard fields and time series output at point locations from TC tracks.  R's compatibility to simply use fast 'cpp' code via the 'Rcpp' package and the wide range spatial analysis tools via the 'terra' package makes it an attractive open source environment to study 'TCs'.  This package estimates TC vortex wind and pressure fields using parametric equations originally coded up in 'python' by 'TCRM' <https://github.com/GeoscienceAustralia/tcrm> and then coded up in 'Cuda' 'cpp' by 'TCwindgen' <https://github.com/CyprienBosserelle/TCwindgen>.
	"""
	
	homepage = "https://github.com/AusClimateService/TCHazaRds"
	cran = "TCHazaRds" 

	version("1.0", md5="d7ced4801e64e32d0f7391a450224c66")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
