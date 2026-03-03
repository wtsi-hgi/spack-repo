# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrip(RPackage):
	"""Tracking Data

	Access and manipulate spatial tracking data, with straightforward 
 coercion from and to other formats. Filter for speed and create time spent 
 maps from tracking data. There are coercion methods to convert between 'trip'
 and 'ltraj' from 'adehabitatLT', and between 'trip' and 'psp' and 'ppp' from 
 'spatstat'. Trip objects can be created from raw or grouped data frames, and 
 from types in the 'sp', sf', 'amt', 'trackeR', 'mousetrap', and other packages, 
 Sumner, MD (2011) <https://figshare.utas.edu.au/articles/thesis/The_tag_location_problem/23209538>.
	"""
	
	homepage = "https://github.com/Trackage/trip"
	cran = "trip" 

	version("1.10.0", md5="26c10c07e5fb27874d404d0d9c529352")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reproj", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-traipse@0.2:", type=("build", "run"))
	depends_on("r-crsmeta", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
