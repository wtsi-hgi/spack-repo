# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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
	version("0.6-1", sha256="1f78db3adab9ebbfc9d98c6cc592708d893b5d7fd7fd876af454042ef42204a7")
	version("0.5-6", sha256="e0413c95423635f7f7b2520813382e911257da8ace9b743da9fe3eab568a9461")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-sf@1.0.10:", type=("build", "run"))
	depends_on("r-classint@0.4.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
