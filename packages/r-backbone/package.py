# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBackbone(RPackage):
	"""Extracts the Backbone from Graphs

	An implementation of methods for extracting an unweighted unipartite
   graph (i.e. a backbone) from an unweighted unipartite graph, a weighted unipartite
   graph, the projection of an unweighted bipartite graph, or the projection
   of a weighted bipartite graph (Neal, 2022 <doi:10.1371/journal.pone.0269137>).
	"""
	
	homepage = "https://www.zacharyneal.com/backbone"
	cran = "backbone" 

	version("2.1.3", md5="6bc59fdd97661a5931dd41e576fe0dc3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
