# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterlist(RPackage):
	"""A Raster Where Cells are Generic Objects

	A S4 class has been created such that complex operations can be
    executed on each cell of a raster map. The raster of objects contains a raster map with the addition of a list of generic objects: one
    object for each raster cells. It allows to write few lines of R code for complex
    map algebra. Two environmental applications about frequency analysis of raster
    map of precipitation and creation of a raster map of soil water retention curves
    have been presented.
	"""
	
	homepage = "https://github.com/ecor/rasterList"
	cran = "rasterList" 

	version("0.5.20", md5="3153f8dbf377938de04d98792c61d623")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
