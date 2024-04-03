# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcgeocoder(RPackage):
	"""Geocoding with the 'ArcGIS' REST API Service

	Lite interface for finding locations of addresses or
    businesses around the world using the 'ArcGIS' REST API service
    <https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm>.
    Address text can be converted to location candidates and a location
    can be converted into an address. No API key required.
	"""
	
	homepage = "https://dieghernan.github.io/arcgeocoder/"
	cran = "arcgeocoder" 

	version("0.1.0", md5="72f6f5868b59795e1973e8a6af0b136c")
	version("0.2.0", md5="6ad16da4cc611824370e90d32360410f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
