# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabularaster(RPackage):
	"""Tidy Tools for 'Raster' Data

	Facilities to work with vector and raster data in efficient 
 repeatable and systematic work flow. Missing functionality in existing packages 
 is included here to allow extraction from raster data with 'simple features' and 
 'Spatial' types and to make extraction consistent and straightforward. Extract cell 
 numbers from raster data and  return the cells as a data frame 
 rather than as lists of matrices or vectors. The functions here allow spatial data 
 to be used without special handling for the format currently in use. 
	"""
	
	homepage = "https://github.com/hypertidy/tabularaster"
	cran = "tabularaster" 

	version("0.7.2", md5="5f2386f80bad0a5604faf4d6f659f194")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fasterize", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-silicate", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
