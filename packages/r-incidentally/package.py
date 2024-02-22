# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncidentally(RPackage):
	"""Generates Incidence Matrices and Bipartite Graphs

	Functions to generate incidence matrices and bipartite graphs that have (1) a fixed fill rate, (2) given marginal sums, (3) marginal sums that follow given distributions, or (4) represent bill sponsorships in the US Congress <doi:10.31219/osf.io/ectms>. It can also generate an incidence matrix from an adjacency matrix, or bipartite graph from a unipartite graph, via a social process mirroring team, group, or organization formation <doi:10.48550/arXiv.2204.13670>.
	"""
	
	homepage = "https://www.zacharyneal.com/backbone"
	cran = "incidentally" 

	version("1.0.2", md5="94913d67b87c08139410ccd4b1ad823b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
