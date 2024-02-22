# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItnr(RPackage):
	"""Analysis of the International Trade Network

	Functions to clean and process international trade data into an international trade network (ITN) are provided. It then provides a set a functions to undertake analysis and plots of the ITN (extract the backbone, centrality, blockmodels, clustering). Examining the key players in the ITN and regional trade patterns. 
	"""
	
	cran = "ITNr" 

	version("0.7.0", md5="3a30ccd2945f4dced27f8fab63792d21")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-xergm-common", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-blockmodeling", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-tnet", type=("build", "run"))
	depends_on("r-wdi", type=("build", "run"))
	depends_on("r-networkdynamic", type=("build", "run"))
