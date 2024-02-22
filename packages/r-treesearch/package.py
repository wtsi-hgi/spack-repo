# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreesearch(RPackage):
	"""Phylogenetic Analysis with Discrete Character Data

	Reconstruct phylogenetic trees from discrete data.
  Inapplicable character states are handled using the algorithm of Brazeau,
  Guillerme and Smith (2019) <doi:10.1093/sysbio/syy083> with the "Morphy"
  library, under equal or implied step weights.
  Contains a "shiny" user interface for interactive tree search and exploration
  of results, including character visualization, rogue taxon detection,
  tree space mapping, and cluster consensus trees (Smith 2022a, b)
  <doi:10.1093/sysbio/syab099>, <doi:10.1093/sysbio/syab100>.
  Profile Parsimony (Faith and Trueman, 2001) <doi:10.1080/10635150118627>, 
  Successive Approximations (Farris, 1969) <doi:10.2307/2412182>
  and custom optimality criteria are implemented.
	"""
	
	homepage = "https://ms609.github.io/TreeSearch/"
	cran = "TreeSearch" 

	version("1.4.0", md5="955c0eb0a6bedb61f27c24bdd1f5722d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape@5.6:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fastmatch@1.1.3:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-plottools", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-protoclust", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-rogue@2:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-treedist@2.6.3:", type=("build", "run"))
	depends_on("r-treetools", type=("build", "run"))
