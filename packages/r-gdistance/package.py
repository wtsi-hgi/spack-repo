# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdistance(RPackage):
	"""Distances and Routes on Geographical Grids

	Provides classes and functions to calculate various 
             distance measures and routes in heterogeneous geographic 
             spaces represented as grids. The package implements measures
             to model dispersal histories first presented by van Etten and
             Hijmans (2010) <doi:10.1371/journal.pone.0012060>. Least-cost
             distances as well as more complex distances based on (constrained)
             random walks can be calculated. The distances implemented in 
             the package are used in geographical genetics, accessibility 
             indicators, and may also have applications in other fields of
             geospatial analysis.
	"""
	
	homepage = "https://AgrDataSci.github.io/gdistance/"
	cran = "gdistance" 

	version("1.6.4", md5="b05db220814b6d2a5a4511dc33522d5c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-raster@1.9.19:", type=("build", "run"))
	depends_on("r-igraph@0.7:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
