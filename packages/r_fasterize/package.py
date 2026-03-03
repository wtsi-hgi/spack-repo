# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasterize(RPackage):
	"""Fast Polygon to Raster Conversion

	Provides a drop-in replacement for rasterize() from the 'raster'
   package that takes polygon vector or data frame objects, and is much faster. 
   There is support for the main options provided by the rasterize() function, 
   including setting the field used and background value, and options for 
   aggregating multi-layer rasters. Uses the scan line algorithm attributed to
   Wylie et al. (1967) <doi:10.1145/1465611.1465619>.
	"""
	
	homepage = "https://github.com/ecohealthalliance/fasterize"
	cran = "fasterize" 

	version("1.0.5", md5="d01c6f7812d6c83987588d4f06e9746c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster@2.8.3:", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
