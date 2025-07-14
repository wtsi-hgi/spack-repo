# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcigraph(RPackage):
	"""Pathways from the NCI Pathways Database

	Provides various methods to load the pathways from the NCI Pathways Database in R graph objects and to re-format them.
	"""
	
	bioc = "NCIgraph"

	version("1.56.0", commit="7a42ff77f66cf5ac9b002557a2e96acd03ffa9a2")
	version("1.50.0", commit="fc6019c20cc6ab83663fe27a1b2a39eaab286019")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
