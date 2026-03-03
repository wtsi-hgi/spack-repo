# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWkb(RPackage):
	"""Convert Between Spatial Objects and Well-Known Binary Geometry

	Utility functions to convert between the 'Spatial' classes
  specified by the package 'sp', and the well-known binary '(WKB)'
  representation for geometry specified by the 'Open Geospatial Consortium'.
  Supports 'Spatial' objects of class 'SpatialPoints',
  'SpatialPointsDataFrame', 'SpatialLines', 'SpatialLinesDataFrame',
  'SpatialPolygons', and 'SpatialPolygonsDataFrame'. Supports 'WKB' geometry
  types 'Point', 'LineString', 'Polygon', 'MultiPoint', 'MultiLineString', and
  'MultiPolygon'. Includes extensions to enable creation of maps with
  'TIBCO Spotfire'.
	"""
	
	cran = "wkb" 

	version("0.4-0", md5="f1b5ceb10434779a19067541333281eb")

	depends_on("r-sp", type=("build", "run"))
