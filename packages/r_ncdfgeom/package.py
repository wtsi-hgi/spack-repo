# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcdfgeom(RPackage):
	"""'NetCDF' Geometry and Time Series

	Tools to create time series and geometry 'NetCDF' files.
	"""
	
	homepage = "https://code.usgs.gov/water/ncdfgeom"
	cran = "ncdfgeom" 

	version("1.1.6", md5="0148eefa1145b10ad82db50671f8dc4c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rnetcdf", type=("build", "run"))
	depends_on("r-ncmeta", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-areal", type=("build", "run"))
