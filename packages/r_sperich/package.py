# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSperich(RPackage):
	"""Auxiliary Functions to Estimate Centers of Biodiversity

	Provides some easy-to-use functions to interpolate species range based on species occurrences and to estimate centers of biodiversity.
	"""
	
	cran = "sperich" 

	version("1.5-9", md5="c5f43790a0890d3356032115f283256a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
