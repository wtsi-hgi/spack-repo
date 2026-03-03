# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeohashtools(RPackage):
	"""Tools for Working with Geohashes

	Tools for working with Gustavo Niemeyer's geohash coordinate system, including API for interacting with other common R GIS libraries.
	"""
	
	homepage = "https://github.com/MichaelChirico/geohashTools"
	cran = "geohashTools" 

	version("0.3.3", md5="54fdf00ce3f9368d9bafa00a3ac7e9ca")

	depends_on("r@3:", type=("build", "run"))
