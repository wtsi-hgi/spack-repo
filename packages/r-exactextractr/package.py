# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactextractr(RPackage):
	"""Fast Extraction from Raster Datasets using Polygons.

	Provides a replacement for the 'extract' function from the 'raster' package
	that is suitable for extracting raster values using 'sf' polygons."""

	cran = "exactextractr"

	version("0.10.0", md5="cc86e567b376f84de4a4d91d0cc1cd05")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))
	depends_on("geos@3.5.0:", type=("build", "link", "run"))
