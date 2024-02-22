# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodata(RPackage):
	"""Download Geographic Data

	Functions for downloading of geographic data for use in spatial analysis and mapping. The package facilitates access to climate, crops, elevation, land use, soil, species occurrence, accessibility, administrative boundaries and other data.
	"""
	
	cran = "geodata" 

	version("0.5-9", md5="8b260160a762b866cf1b59fd0ca69bd0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra@1.6.41:", type=("build", "run"))
