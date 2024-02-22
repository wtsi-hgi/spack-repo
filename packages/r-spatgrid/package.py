# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatgrid(RPackage):
	"""Spatial Grid Generation from Longitude and Latitude List

	The developed function is designed for the generation of spatial grids based on user-specified longitude and latitude coordinates. The function first validates the input longitude and latitude values,
              ensuring they fall within the appropriate geographic ranges. It then creates a polygon from the coordinates and determines the appropriate Universal Transverse Mercator zone based on the provided 
              hemisphere and longitude values. Subsequently, transforming the input Shapefile to the Universal Transverse Mercator projection when necessary. Finally, a spatial grid is generated with the specified interval and saved as a Shapefile. 
              For method details see, Brus,D.J.(2022).<DOI:10.1201/9781003258940>. The function takes into account crucial parameters such as the hemisphere (north or south), desired grid interval, and the output Shapefile path.
              The developed function is an efficient tool, simplifying the process of empty spatial grid generation for applications such as, geo-statistical analysis, digital soil mapping product generation, etc. Whether for environmental studies, 
              urban planning, or any other geo-spatial analysis, this package caters to the diverse needs of users working with spatial data, enhancing the accessibility and ease of spatial data processing and visualization.
	"""
	
	cran = "SpatGRID" 

	version("0.1.0", md5="1310febccba490ef7d2f8dbf54e35b29")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
