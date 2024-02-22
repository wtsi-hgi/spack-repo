# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsom(RPackage):
	"""Using self-organizing maps for visualization and interpretation of cytometry data

	FlowSOM offers visualization options for cytometry data, by using Self-Organizing Map clustering and Minimal Spanning Trees.
	"""
	
	homepage = "http://www.r-project.org"
	bioc = "FlowSOM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/FlowSOM_2.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/FlowSOM/FlowSOM_2.10.0.tar.gz"]

	version("2.10.0", md5="9bc309cc9948473d101d91ba6f1a37f2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
