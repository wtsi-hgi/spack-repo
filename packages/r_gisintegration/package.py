# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGisintegration(RPackage):
	"""GIS Integration

	Designed to facilitate the preprocessing and linking of GIS (Geographic Information System) databases
  <https://www.sciencedirect.com/topics/computer-science/gis-database>,
  the R package 'GISINTEGRATION' offers a robust solution for efficiently preparing  GIS data for advanced 
  spatial analyses. This package excels in simplifying intrica  procedures like data cleaning, normalization, 
  and format conversion, ensuring that the data are optimally primed for precise and thorough analysis.
	"""
	
	cran = "GISINTEGRATION" 

	version("1.0", md5="d5f61fa3328e8e750e8ba69acc267cca")

	depends_on("r-shapefiles", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-syn", type=("build", "run"))
	depends_on("r-recordlinkage", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
