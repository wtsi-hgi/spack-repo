# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdalraster(RPackage):
	"""Bindings to the 'Geospatial Data Abstraction Library' Raster API

	Interface to the Raster API of the 'Geospatial Data Abstraction
    Library' ('GDAL', <https://gdal.org>). Bindings are implemented in an
    exposed C++ class encapsulating a 'GDALDataset' and its raster band
    objects, along with several stand-alone functions. These support manual
    creation of uninitialized datasets, creation from existing raster as
    template, read/set dataset parameters, low level I/O, color tables, raster 
    attribute tables, virtual raster (VRT), and 'gdalwarp' wrapper for
    reprojection and mosaicing. Includes 'GDAL' algorithms ('dem_proc()',
    'polygonize()', 'rasterize()', etc.), and functions for coordinate
    transformation and spatial reference systems. Calling signatures resemble
    the native C, C++ and Python APIs provided by the 'GDAL' project. Includes
    raster 'calc()' to evaluate a given R expression on a layer or stack of
    layers, with pixel x/y available as variables in the expression; and raster
    'combine()' to identify and count unique pixel combinations across multiple
    input layers, with optional output of the pixel-level combination IDs.
    Provides raster display using base 'graphics'. Bindings to a subset of
    the Virtual Systems Interface ('VSI') are also included to support
    operations on 'GDAL' virtual file systems. These are general utility
    functions that abstract file system operations on URLs, cloud storage
    services, 'Zip'/'GZip'/'7z'/'RAR' archives, and in-memory files.
    'gdalraster' may be useful in applications that need scalable, low-level
    I/O, or prefer a direct 'GDAL' API.
	"""
	
	homepage = "https://usdaforestservice.github.io/gdalraster/"
	cran = "gdalraster" 

	version("1.9.0", md5="a6ef7f65c300c69b644242454d2c2d92")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("gdal@2.4.0:", type=("build", "link", "run"))
	depends_on("proj", type=("build", "link", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
