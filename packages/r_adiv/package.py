# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdiv(RPackage):
	"""Analysis of Diversity

	Functions, data sets and examples for the calculation of various indices of biodiversity including species, functional and phylogenetic diversity. Part of the indices are expressed in terms of equivalent numbers of species. The package also provides ways to partition biodiversity across spatial or temporal scales (alpha, beta, gamma diversities). In addition to the quantification of biodiversity, ordination approaches are available which rely on diversity indices and allow the detailed identification of species, functional or phylogenetic differences between communities.
	"""
	
	cran = "adiv" 

	version("2.2.1", md5="88e3a0e6fe27e027cfca0f379180b4ed")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-adegraphics", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
