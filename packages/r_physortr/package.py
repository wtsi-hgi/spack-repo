# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhysortr(RPackage):
	"""A Fast, Flexible Tool for Sorting Phylogenetic Trees

	Screens and sorts phylogenetic trees in both traditional and
    extended Newick format. Allows for the fast and flexible screening (within
    a tree) of Exclusive clades that comprise only the target taxa and/or Non-
    Exclusive clades that includes a defined portion of non-target taxa.
	"""
	
	cran = "PhySortR" 

	version("1.0.8", md5="76a1debe294547b9b25d45c065511ff7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
