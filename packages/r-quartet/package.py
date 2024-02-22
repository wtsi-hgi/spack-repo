# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuartet(RPackage):
	"""Comparison of Phylogenetic Trees Using Quartet and Split
Measures

	Calculates the number of four-taxon subtrees consistent with a pair
  of cladograms, calculating the symmetric quartet distance of Bandelt & Dress
  (1986), Reconstructing the shape of a tree from observed dissimilarity data,
  Advances in Applied Mathematics, 7, 309-343 <doi:10.1016/0196-8858(86)90038-2>, 
  and using the tqDist algorithm of Sand et al. (2014), tqDist: a library for
  computing the quartet and triplet distances between binary or general trees,
  Bioinformatics, 30, 2079–2080 <doi:10.1093/bioinformatics/btu157>
  for pairs of binary trees.
	"""
	
	homepage = "https://ms609.github.io/Quartet/"
	cran = "Quartet" 

	version("1.2.6", md5="e1108c1a7340e560bdeadef946bcaff5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-treetools@1.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-ternary@1:", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
