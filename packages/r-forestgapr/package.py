# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestgapr(RPackage):
	"""Tropical Forest Canopy Gaps Analysis

	Set of tools for detecting and analyzing Airborne Laser Scanning-derived Tropical Forest Canopy Gaps. Details were published in Silva and others (2019) <doi:10.1111/2041-210X.13211>.
	"""
	
	cran = "ForestGapR" 

	version("0.1.7", md5="204daed569cd22cdaa57d277b2293657")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-powerlaw", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
