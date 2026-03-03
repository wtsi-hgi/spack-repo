# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapiso(RPackage):
	"""Create Contour Polygons from Regular Grids

	Regularly spaced grids containing continuous data are transformed
    to contour polygons. A grid can be defined by a data.frame (x, y, value),
    an 'sf' object or a raster from 'terra'.
	"""
	
	homepage = "https://github.com/riatelab/mapiso"
	cran = "mapiso" 

	version("0.3.0", md5="4da01af9a6e1cd5958ea018eac349a26")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
