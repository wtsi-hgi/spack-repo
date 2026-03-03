# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApoderoides(RPackage):
	"""Prioritize and Delete Erroneous Taxa in a Large Phylogenetic
Tree

	Finds, prioritizes and deletes erroneous taxa in a phylogenetic tree. This package calculates scores for taxa in a tree. Higher score means the taxon is more erroneous. If the score is zero for a taxon, the taxon is not erroneous. This package also can remove all erroneous taxa automatically by iterating score calculation and pruning taxa with the highest score.
	"""
	
	homepage = "https://github.com/Sa-to-shi-A-o-ki/Apoderoides"
	cran = "Apoderoides" 

	version("1.0.1", md5="ad21680258e57e4c1a64ff82e65f1857")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
