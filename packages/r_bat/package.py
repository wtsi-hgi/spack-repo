# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBat(RPackage):
	"""Biodiversity Assessment Tools

	Includes algorithms to assess alpha and beta diversity
    in all their dimensions (taxonomic, phylogenetic and functional).
    It allows performing a number of analyses based on species
    identities/abundances, phylogenetic/functional distances, trees,
    convex-hulls or kernel density n-dimensional hypervolumes
    depicting species relationships.
    Cardoso et al. (2015) <doi:10.1111/2041-210X.12310>.
	"""
	
	cran = "BAT" 

	version("2.9.6", md5="d1aca8b37e6c8141feb08290a480cc06")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-hypervolume", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
