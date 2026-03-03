# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraipse(RPackage):
	"""Shared Tools for Tracking Data

	A collection of commonly used tools for animal movement and other tracking 
 data. Variously distance, angle, bearing, distance-to, bearing-to and speed are 
 provided for geographic data that can be used directly or within 'tidyverse' 
 syntax. Distances and bearings are calculated using modern geodesic methods as 
 provided by Charles F. F. Karney (2013) <doi:10.1007/s00190-012-0578-z> 
 via the 'geodist' and 'geosphere' packages. 
	"""
	
	homepage = "https://github.com/Trackage/traipse"
	cran = "traipse" 

	version("0.3.0", md5="a578cd5d96c1f6bb94822c7cdbe492d2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
