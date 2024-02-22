# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandgeo(RPackage):
	"""Generate Random 'WKT' or 'GeoJSON'

	Generate random positions (latitude/longitude), 
    Well-known text ('WKT') points or polygons, or 'GeoJSON' points or 
    polygons. 
	"""
	
	homepage = "https://github.com/ropensci/randgeo"
	cran = "randgeo" 

	version("0.3.0", md5="e12bbdd394b8fcbd65eabf7e89cf17d7")

