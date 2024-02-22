# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemgene(RPackage):
	"""Spatial Pattern Detection in Genetic Distance Data Using Moran's
Eigenvector Maps

	Can detect relatively weak spatial genetic patterns by using Moran's Eigenvector Maps (MEM) to extract only the spatial component of genetic variation.  Has applications in landscape genetics where the movement and dispersal of organisms are studied using neutral genetic variation.
	"""
	
	cran = "memgene" 

	version("1.0.2", md5="d619dc4abf5017a9aec8431bf4e2b527")

	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
