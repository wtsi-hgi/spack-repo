# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellnoptr(RPackage):
	"""Training of boolean logic models of signalling networks using prior knowledge networks and perturbation data

	This package does optimisation of boolean logic networks of signalling pathways based on a previous knowledge network and a set of data upon perturbation of the nodes in the network.
	"""
	
	bioc = "CellNOptR"

	version("1.54.0", commit="c2d1b49b5b93ae58d9b1e9073a8223714497074a")
	version("1.48.0", commit="0a9b48858e2987c8610f013a6a42a576b616975b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("graphviz@2.2:", type=("build", "link", "run"))
