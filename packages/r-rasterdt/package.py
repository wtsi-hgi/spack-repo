# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterdt(RPackage):
	"""Fast Raster Summary and Manipulation

	
  Fast alternatives to several relatively slow 'raster' package
  functions. For large rasters, the functions run from 5 to
  approximately 100 times faster than the 'raster' package functions
  they replace. The 'fasterize' package, on which one function in this
  package depends, includes an implementation of the scan line
  algorithm attributed to Wylie et al. (1967)
  <doi:10.1145/1465611.1465619>.
	"""
	
	homepage = "https://github.com/JoshOBrien/rasterDT/"
	cran = "rasterDT" 

	version("0.3.2", md5="0b8fc9d112950837b2010cc14be8bc7e")

	depends_on("r-raster@3.6.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fasterize", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
