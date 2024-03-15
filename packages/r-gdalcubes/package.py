# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdalcubes(RPackage):
	"""Earth Observation Data Cubes from Satellite Image Collections

	Processing collections of Earth observation images as on-demand multispectral, multitemporal raster data cubes. Users
    define cubes by spatiotemporal extent, resolution, and spatial reference system and let 'gdalcubes' automatically apply cropping, reprojection, and 
    resampling using the 'Geospatial Data Abstraction Library' ('GDAL'). Implemented functions on data cubes include reduction over space and time, 
    applying arithmetic expressions on pixel band values, moving window aggregates over time, filtering by space, time, bands, and predicates on pixel values, 
    exporting data cubes as 'netCDF' or 'GeoTIFF' files, plotting, and extraction from spatial and or spatiotemporal features.  
    All computational parts are implemented in C++, linking to the 'GDAL', 'netCDF', 'CURL', and 'SQLite' libraries. 
    See Appel and Pebesma (2019) <doi:10.3390/data4030092> for further details.
	"""
	
	homepage = "https://github.com/appelmar/gdalcubes"
	cran = "gdalcubes" 

	version("0.7.0", md5="e77b9a38651d32c8d885a077d5909537")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
	depends_on("netcdf-c", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
