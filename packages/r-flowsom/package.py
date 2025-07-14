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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FlowSOM_2.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FlowSOM/FlowSOM_2.10.0.tar.gz"]

	version("2.16.0", tag="RELEASE_3_21")
	version("2.10.0", sha256="74d4f46e6b3928affca83628d030f9b5cd8624993b7d9723be5dbb49d6f81d9c")

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
