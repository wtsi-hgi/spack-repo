# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiler(RPackage):
	"""Create Geographic and Non-Geographic Map Tiles

	Creates geographic map tiles from geospatial map files or 
    non-geographic map tiles from simple image files. This package provides a 
    tile generator function for creating map tile sets for use with packages 
    such as 'leaflet'. In addition to generating map tiles based on a common 
    raster layer source, it also handles the non-geographic edge case, producing 
    map tiles from arbitrary images. These map tiles, which have a 
    non-geographic, simple coordinate reference system (CRS), can also be used 
    with 'leaflet' when applying the simple CRS option. Map tiles can be created 
    from an input file with any of the following extensions: tif, grd and nc for 
    spatial maps and png, jpg and bmp for basic images. This package requires 
    'Python' and the 'gdal' library for 'Python'. 'Windows' users are 
    recommended to install 'OSGeo4W' (<https://trac.osgeo.org/osgeo4w/>) as an 
    easy way to obtain the required 'gdal' support for 'Python'.
	"""
	
	homepage = "https://docs.ropensci.org/tiler/"
	cran = "tiler" 

	version("0.3.1", md5="96413e0980f4c39f585b311aee79aba3")

	depends_on("r-png", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
	depends_on("py-pygdal", type=("build", "link", "run"))
