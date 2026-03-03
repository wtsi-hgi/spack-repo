# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimclass(RPackage):
	"""Climate Classification According to Several Indices

	Classification of climate according to Koeppen - Geiger, of aridity
    indices, of continentality indices, of water balance after Thornthwaite, of
    viticultural bioclimatic indices. Drawing climographs: Thornthwaite, Peguy,
    Bagnouls-Gaussen.
	"""
	
	cran = "ClimClass" 

	version("2.1.0", md5="c0e4347a8a3d345196aaa209e838bef2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
