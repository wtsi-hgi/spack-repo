# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraticule(RPackage):
	"""Meridional and Parallel Lines for Maps

	Create graticule lines and labels for maps. Control the creation
    of lines or tiles by setting their placement (at particular meridians and parallels)
    and extent (along parallels and meridians). Labels are created independently of
    lines.
	"""
	
	homepage = "https://github.com/hypertidy/graticule"
	cran = "graticule" 

	version("0.4.0", md5="423fbb3c551c7891b31cf6b7693dae42")

	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-reproj@0.4.3:", type=("build", "run"))
