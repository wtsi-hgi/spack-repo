# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosstalkr(RPackage):
	"""Analysis of Graph-Structured Data with a Focus on
Protein-Protein Interaction Networks

	Provides a general toolkit for drug target identification. We include functionality to reduce large graphs to subgraphs and prioritize nodes. In addition to being optimized for use with generic graphs, we also provides support to analyze protein-protein interactions networks from online repositories. For more details on core method, refer to Weaver et al. (2021) <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008755>.
	"""
	
	cran = "crosstalkr" 

	version("1.0.4", md5="76f15b6833d2110e69795dab64e303e5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-igraph@1.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
