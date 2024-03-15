# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClipper(RPackage):
	"""Gene Set Analysis Exploiting Pathway Topology

	Implements topological gene set analysis using a two-step empirical approach. It exploits graph decomposition theory to create a junction tree and reconstruct the most relevant signal path. In the first step clipper selects significant pathways according to statistical tests on the means and the concentration matrices of the graphs derived from pathway topologies. Then, it "clips" the whole pathway identifying the signal paths having the greatest association with a specific phenotype.
	"""
	
	bioc = "clipper" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clipper_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clipper/clipper_1.42.0.tar.gz"]

	version("1.42.0", md5="551f3c6ad3a56f2a70439f48a4aef431")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-grbase@1.6.6:", type=("build", "run"))
	depends_on("r-qpgraph", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
