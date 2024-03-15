# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTerra(RPackage):
	"""Spatial Data Analysis.

	Methods for spatial data analysis with raster and vector data. Raster
	methods allow for low-level data manipulation as well as high-level global,
	local, zonal, and focal computation. The predict and interpolate methods
	facilitate the use of regression type (interpolation, machine learning)
	models for spatial prediction, including with satellite remote sensing
	data. Processing of very large files is supported. See the manual and
	tutorials on <https://rspatial.org/terra/> to get started. 'terra' is very
	similar to the 'raster' package; but 'terra' can do more, is easier to use,
	and it is faster."""

	cran = "terra"

	license("GPL-3.0-or-later")

	version("1.7-71", md5="1f77a38039a013b8301b0884b2a380e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("gdal@2.2.3:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.9.3:", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
