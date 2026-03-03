# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfdct(RPackage):
	"""Constrained Triangulation for Simple Features

	Build a constrained high quality Delaunay triangulation from simple 
   features objects, applying constraints based on input line segments, and 
   triangle properties including maximum area, minimum internal angle. The 
   triangulation code in 'RTriangle' uses the method of Cheng, Dey and Shewchuk 
   (2012, ISBN:9781584887300). For a low-dependency alternative with low-quality 
   path-based constrained  triangulation see <https://CRAN.R-project.org/package=decido> and for high-quality configurable
    triangulation see <https://github.com/hypertidy/anglr>. Also consider comparison
    with the 'GEOS' lib which since version 3.10.0 includes a low quality 
    polygon triangulation method that starts with ear clipping and refines to Delaunay. 
	"""
	
	homepage = "https://github.com/hypertidy/sfdct"
	cran = "sfdct" 

	version("0.3.0", md5="6a824e8c04130662a1864ec06f04910c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rtriangle", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
