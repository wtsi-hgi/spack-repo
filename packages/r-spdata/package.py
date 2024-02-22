# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpdata(RPackage):
	"""Datasets for Spatial Analysis.

	Diverse spatial datasets for demonstrating, benchmarking and teaching
	spatial data analysis.  It includes R data of class sf (defined by the
	package 'sf'), Spatial ('sp'), and nb ('spdep'). Unlike other spatial data
	packages such as 'rnaturalearth' and 'maps',  it also contains data stored
	in a range of file formats including GeoJSON, ESRI Shapefile and
	GeoPackage.  Some of the datasets are designed to illustrate specific
	analysis techniques. cycle_hire() and cycle_hire_osm(), for example, is
	designed to illustrate point pattern analysis techniques."""

	cran = "spData"

	version("2.3.0", md5="41aae4a68e1e038d28ff80af8388ee8f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
