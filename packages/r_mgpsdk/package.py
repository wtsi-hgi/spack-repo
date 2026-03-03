# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgpsdk(RPackage):
	"""Interact with the Maxar 'MGP' Application Programming Interfaces

	Provides an interface to the Maxar Geospatial Platform (MGP) Application Programming Interface. <https://www.maxar.com/maxar-geospatial-platform>
    It facilitates imagery searches using the MGP Streaming Application Programming Interface via the Web Feature Service (WFS) method, and supports image downloads through Web Map Service (WMS) and Web Map Tile Service (WMTS)
    Open Geospatial Consortium (OGC) methods. 
    Additionally, it integrates with the Maxar Geospatial Platform Basemaps Application Programming Interface for accessing Maxar basemaps imagery and seamlines. 
    The package also offers seamless integration with the Maxar Geospatial Platform Discovery Application Programming Interface, allowing users to search, filter, and sort Maxar content, 
    while retrieving detailed metadata in formats like SpatioTemporal Asset Catalog (STAC) and GeoJSON.
	"""
	
	cran = "MGPSDK" 

	version("1.0.0", md5="a392534e630b9022baa6ba528b4a0ce1")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
