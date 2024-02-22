# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaster(RPackage):
	"""Geographic Data Analysis and Modeling.

	Reading, writing, manipulating, analyzing and modeling of spatial data. The
	package implements basic and high-level functions for raster data and for
	vector data operations such as intersections. See the manual and tutorials
	on <https://rspatial.org/> to get started."""

	cran = "raster"

	version("3.6-26", md5="ad7c711017003e97af9828e1547d14ab")

	depends_on("r-sp@1.4.5:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra@1.7.29:", type=("build", "run"))
