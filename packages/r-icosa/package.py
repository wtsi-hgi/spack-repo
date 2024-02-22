# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcosa(RPackage):
	"""Global Triangular and Penta-Hexagonal Grids Based on Tessellated
Icosahedra

	Implementation of icosahedral grids in three dimensions. The spherical-triangular tessellation can be set to create grids with custom resolutions. Both the primary triangular and their inverted penta-hexagonal grids can be calculated. Additional functions are provided that allow plotting of the grids and associated data, the interaction of the grids with other raster and vector objects, and treating the grids as a graphs.
	"""
	
	homepage = "https://adamkocsis.github.io/icosa/"
	cran = "icosa" 

	version("0.11.0", md5="7e11846b16f4353e21f06e818814acba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
