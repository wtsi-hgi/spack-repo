# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyperdraw(RPackage):
	"""Visualizing Hypergaphs

	Functions for visualizing hypergraphs.
	"""
	
	bioc = "hyperdraw"

	version("1.60.0", commit="56af00acb1937aaa56b022b5a80778cf9e6d4d92")
	version("1.54.0", commit="0a7e984f58fca576c9c8a9ef9f7b4eb1d9904c88")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-hypergraph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("graphviz", type=("build", "link", "run"))
