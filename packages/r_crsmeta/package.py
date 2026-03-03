# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrsmeta(RPackage):
	"""Extract Coordinate System Metadata

	Obtain coordinate system metadata from various data formats. There 
 are functions to extract a 'CRS' (coordinate reference system, 
 <https://en.wikipedia.org/wiki/Spatial_reference_system>) in 'EPSG' (European 
 Petroleum Survey Group, <http://www.epsg.org/>), 'PROJ4' <https://proj.org/>, 
 or 'WKT2' (Well-Known Text 2, 
 <http://docs.opengeospatial.org/is/12-063r5/12-063r5.html>) forms. This is 
 purely for getting simple metadata from in-memory formats, please use other 
 tools for out of memory data sources. 
	"""
	
	homepage = "https://github.com/hypertidy/crsmeta"
	cran = "crsmeta" 

	version("0.3.0", md5="2f31751c6b00fdfcfc9c5ad186c49aa3")

	depends_on("r@3.5:", type=("build", "run"))
