# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRogue(RPackage):
	"""Identify Rogue Taxa in Sets of Phylogenetic Trees

	Rogue ("wildcard") taxa are leaves with uncertain phylogenetic
  position.
  Their position may vary from tree to tree under inference methods that yield a
  tree set (e.g. bootstrapping, Bayesian tree searches, maximum parsimony).
  The presence of rogue taxa in a tree set can potentially remove all
  information from a consensus tree. The information content of a consensus
  tree - a function of its resolution and branch support values - can often be
  increased by removing rogue taxa. 
  'Rogue' provides an explicitly information-theoretic approach to rogue
  detection (Smith 2022) <doi:10.1093/sysbio/syab099>,
  and an interface to 'RogueNaRok' (Aberer et al. 2013)
  <doi:10.1093/sysbio/sys078>.
	"""
	
	homepage = "https://github.com/ms609/Rogue/"
	cran = "Rogue" 

	version("2.1.6", md5="141a2936bf39e506a24d3f8afff344ef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-treedist@2.2:", type=("build", "run"))
	depends_on("r-treetools@1.9.1.9003:", type=("build", "run"))
