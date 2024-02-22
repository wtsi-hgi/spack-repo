# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsetse(RPackage):
	"""Strain Elevation Tension Spring Embedding

	An R implementation for the Strain Elevation and
    Tension embedding algorithm from Bourne (2020)
    <doi:10.1007/s41109-020-00329-4>. The package embeds graphs and
    networks using the Strain Elevation and Tension embedding (SETSe)
    algorithm. SETSe represents the network as a physical system, where
    edges are elastic, and nodes exert a force either up or down based on
    node features. SETSe positions the nodes vertically such that the
    tension in the edges of a node is equal and opposite to the force it
    exerts for all nodes in the network. The resultant structure can then
    be analysed by looking at the node elevation and the edge strain and
    tension. This algorithm works on weighted and unweighted networks as
    well as networks with or without explicit node features.  Edge
    elasticity can be created from existing edge weights or kept as a
    constant.
	"""
	
	homepage = "https://github.com/JonnoB/rSETSe"
	cran = "rsetse" 

	version("0.5.0", md5="d23e31e4c6088436290cac13c59d1253")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
