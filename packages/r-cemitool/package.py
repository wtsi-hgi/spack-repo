# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCemitool(RPackage):
	"""Co-expression Modules identification Tool

	The CEMiTool package unifies the discovery and the analysis of coexpression gene modules in a fully automatic manner, while providing a user-friendly html report with high quality graphs. Our tool evaluates if modules contain genes that are over-represented by specific pathways or that are altered in a specific sample group. Additionally, CEMiTool is able to integrate transcriptomic data with interactome information, identifying the potential hubs on each network.
	"""
	
	bioc = "CEMiTool" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CEMiTool_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CEMiTool/CEMiTool_1.26.0.tar.gz"]

	version("1.26.0", md5="df823e2602a3b994f889644e39e0eb8f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
