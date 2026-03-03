# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyncsa(RPackage):
	"""Analysis of Functional and Phylogenetic Patterns in
Metacommunities

	Analysis of metacommunities based on functional traits and
    phylogeny of the community components. The functions that are offered here
    implement for the R environment methods that have been available in the
    SYNCSA application written in C++ (by Valerio Pillar, available at 
    <http://ecoqua.ecologia.ufrgs.br/SYNCSA.html>).
	"""
	
	cran = "SYNCSA" 

	version("1.3.4", md5="1af1f6090bf2bbff6d2e941aa78f260c")

	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-fd", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
