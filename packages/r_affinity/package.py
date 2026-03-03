# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffinity(RPackage):
	"""Raster Georeferencing, Grid Affine Transforms, Cell Abstraction

	Tools for raster georeferencing, grid affine transforms, and general raster logic. 
 These functions provide converters between raster specifications, world vector, geotransform, 
 'RasterIO' window, and 'RasterIO window' in 'sf' package list format. There are functions to offset
 a matrix by padding any of four corners (useful for vectorizing neighbourhood operations), and
 helper functions to harvesting user clicks on a graphics device to use for simple georeferencing
 of images.  Methods used are available from <https://en.wikipedia.org/wiki/World_file> and
 <https://gdal.org/user/raster_data_model.html>. 
	"""
	
	homepage = "https://github.com/hypertidy/affinity"
	cran = "affinity" 

	version("0.2.5", md5="b8e7a7826697409b122bfa49df3bfcf9")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reproj", type=("build", "run"))
