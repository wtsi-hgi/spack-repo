# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdalraster(RPackage):
	"""Bindings to the 'Geospatial Data Abstraction Library' Raster API

	Interface to the Raster API of the 'Geospatial Data Abstraction
    Library' ('GDAL') supporting manual creation of uninitialized datasets,
    creation from existing raster as template, low level I/O, configuration of
    virtual raster (VRT), coordinate transformation, and access to 'gdalwarp'
    for reprojection. Includes several 'GDAL' algorithms and functions for
    working with spatial reference systems. Calling signatures resemble the
    native C, C++ and Python APIs provided by the 'GDAL' project
    (<https://gdal.org>). Bindings are implemented via exposed C++ class
    encapsulating a 'GDALDataset' and its associated 'GDALRasterBand' objects,
    plus several stand-alone functions. Additional functionality includes:
    class 'RunningStats' for efficient summary statistics on large data
    streams; class 'CmbTable' for counting unique combinations of integers
    with a hash table; raster 'combine()' to identify and count unique pixel
    combinations across multiple input layers; raster 'calc()' to evaluate
    an R expression on a stack of layers with pixel coordinates available as
    variables in the expression; and raster display using base 'graphics'.
    'gdalraster' may be suitable for applications that primarily need low-level
    I/O or prefer a direct 'GDAL' API. The additional functionality is somewhat
    aimed at thematic data analysis but may have other utility.
	"""
	
	homepage = "https://usdaforestservice.github.io/gdalraster/"
	cran = "gdalraster" 

	version("1.8.0", md5="2ae8b8925cd82504fbbf5f6c78bd206e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("gdal@2.4.0:", type=("build", "link", "run"))
	depends_on("proj", type=("build", "link", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
