# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpex(RPackage):
	"""Spatial Extent Tools

	Functions to produce a fully fledged 'geo-spatial' object extent as a
    'SpatialPolygonsDataFrame'. Also included are functions to generate polygons
    from raster data using 'quadmesh' techniques, a round number buffered extent, and
    general spatial-extent and 'raster-like' extent helpers missing from the originating
    packages. Some latitude-based tools for polar maps are included. 
	"""
	
	homepage = "https://mdsumner.github.io/spex/"
	cran = "spex" 

	version("0.7.1", md5="8c64ae149ee940c67f617f05cd480cca")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-quadmesh", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reproj", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-crsmeta", type=("build", "run"))
