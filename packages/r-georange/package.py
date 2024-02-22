# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeorange(RPackage):
	"""Calculating Geographic Range from Occurrence Data

	Calculates and analyzes six measures of geographic range from a set of longitudinal and latitudinal occurrence data. Measures included are minimum convex hull area, minimum spanning tree distance, longitudinal range, latitudinal range, maximum pairwise great circle distance, and number of X by X degree cells occupied.
	"""
	
	cran = "GeoRange" 

	version("0.1.0", md5="248a8c03a11d0871d2649d3eabc6159f")

	depends_on("r-sp", type=("build", "run"))
	depends_on("r-proj4", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-velociraptr", type=("build", "run"))
