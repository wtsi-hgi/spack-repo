# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCinna(RPackage):
	"""Deciphering Central Informative Nodes in Network Analysis

	Computing, comparing, and demonstrating top informative centrality measures within a network. "CINNA: an R/CRAN package to decipher Central Informative Nodes in Network Analysis" provides a comprehensive overview of the package functionality Ashtiani et al. (2018) <doi:10.1093/bioinformatics/bty819>.
	"""
	
	cran = "CINNA" 

	version("1.2.2", md5="e303fefc4106ef958f1a18bbe28efff1")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-centiserve", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
