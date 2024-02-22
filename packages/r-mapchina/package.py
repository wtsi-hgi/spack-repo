# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapchina(RPackage):
	"""China Administrative Divisions Geospatial Shapefile Data

	Geospatial shapefile data of China administrative divisions to the county/district-level.
	"""
	
	homepage = "https://github.com/xmc811/mapchina"
	cran = "mapchina" 

	version("0.1.0", md5="c676940d51b7c31e3d081a2a005632a1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
