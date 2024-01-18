# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RClustree(RPackage):
	"""Visualise Clusterings at Different Resolutions

	Deciding what resolution to use can be a difficult question when
    approaching a clustering analysis. One way to approach this problem is to
    look at how samples move as the number of clusters increases. This package
    allows you to produce clustering trees, a visualisation for interrogating
    clusterings as resolution increases.
	"""
	
	homepage = "https://github.com/lazappi/clustree"
	cran = "clustree" 

	version("0.5.1", md5="cb1ebbf96c2188e129b40b454a124da3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4.0:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
