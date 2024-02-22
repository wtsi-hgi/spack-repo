# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriversity(RPackage):
	"""Diversity Measures on Tripartite Graphs

	Computing diversity measures on tripartite graphs. This package first implements a parametrized family of such diversity measures which apply on probability distributions. Sometimes called "True Diversity", this family contains famous measures such as the richness, the Shannon entropy, the Herfindahl-Hirschman index, and the Berger-Parker index. Second, the package allows to apply these measures on probability distributions resulting from random walks between the levels of tripartite graphs. By defining an initial distribution at a given level of the graph and a path to follow between the three levels, the probability of the walker's position within the final level is then computed, thus providing a particular instance of diversity to measure.
	"""
	
	cran = "triversity" 

	version("1.0", md5="5459a73bdc00a67985c3da8433bad1c5")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
