# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMigraph(RPackage):
	"""Many Network Measures, Motifs, Members, and Models

	A set of tools for analysing multimodal networks.
   It includes functions for measuring 
   centrality, centralization, cohesion, closure, constraint and diversity,
   as well as for network block-modelling, regression, and diffusion models.
   The package is released as a complement to 
   'Multimodal Political Networks' (2021, ISBN:9781108985000),
   and includes various datasets used in the book.
   Built on the 'manynet' package, all functions operate with matrices, edge lists, 
   and 'igraph', 'network', and 'tidygraph' objects,
   and on one-mode, two-mode (bipartite), and sometimes three-mode networks.
	"""
	
	homepage = "https://stocnet.github.io/migraph/"
	cran = "migraph" 

	version("1.3.4", md5="ecb506ba3f552cc338cf670a2b0db64d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-manynet", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph@1.5:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
