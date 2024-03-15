# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStars(RPackage):
	"""Spatiotemporal Arrays, Raster and Vector Data Cubes.

	Reading, manipulating, writing and plotting spatiotemporal arrays (raster
	and vector data cubes) in 'R', using 'GDAL' bindings provided by 'sf', and
	'NetCDF' bindings by 'ncmeta' and 'RNetCDF'."""

	cran = "stars"

	version("0.6-4", md5="396cf91eb8e8d9c10ffeddd0cb85e1da")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-sf@1.0.10:", type=("build", "run"))
	depends_on("r-classint@0.4.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
