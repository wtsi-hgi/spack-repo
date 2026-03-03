# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsc(RPackage):
	"""Orthodromic Spatial Clustering

	Allows distance based spatial clustering of georeferenced data by implementing the City Clustering Algorithm - CCA. Multiple versions allow clustering for a matrix, raster and single coordinates on a plain (Euclidean distance) or on a sphere (great-circle or orthodromic distance).
	"""
	
	homepage = "https://www.pik-potsdam.de/~kriewald/osc/"
	cran = "osc" 

	version("1.0.5", md5="6863bc3cda2181a6ff44f085b97e3f09")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r@2.14:", type=("build", "run"))
