# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdalbindings(RPackage):
	"""GDAL Classes Wrapper for Reading and Writing Raster Blocks

	Wraps around 'Geospatial' Data Abstraction Library (GDAL) raster
    and band classes for reading and writing directly from RasterBlock in R
    semantic `[[]]` and familiar syntax for accessing RasterBand and
    reading/writing to blocks (see <https://gdal.org/>).
	"""
	
	homepage = "https://github.com/caiohamamura/gdalBindings-R"
	cran = "gdalBindings" 

	version("0.1.17", md5="1a2bfac3793eacdb7e863ee3ff71f68f")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("gdal", type=("build", "link", "run"))
