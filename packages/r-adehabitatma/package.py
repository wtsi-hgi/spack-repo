# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdehabitatma(RPackage):
	"""Tools to Deal with Raster Maps

	A collection of tools to deal with raster maps.
	"""
	
	cran = "adehabitatMA" 

	version("0.3.16", md5="8c4f737241fa734be5603a940ae86270")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
