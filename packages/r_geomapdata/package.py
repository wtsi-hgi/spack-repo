# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomapdata(RPackage):
	"""Data for Topographic and Geologic Mapping

	Data sets included here are for use with package GEOmap. These include world map, USA map, Coso map, Japan Map.
	"""
	
	cran = "geomapdata" 

	version("2.0-2", md5="cc58797c646a84d5a91e6414ff27c83f")

	depends_on("r@2.10:", type=("build", "run"))
