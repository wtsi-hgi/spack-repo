# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAkc(RPackage):
	"""Automatic Knowledge Classification

	A tidy framework for automatic knowledge classification and visualization. Currently, the core functionality of the framework is mainly supported by modularity-based clustering (community detection) in keyword co-occurrence network, and focuses on co-word analysis of bibliometric research. However, the designed functions in 'akc' are general, and could be extended to solve other tasks in text mining as well.
	"""
	
	homepage = "https://github.com/hope-data-science/akc"
	cran = "akc" 

	version("0.9.9", md5="412015beecfd875bc1063e9fd751758d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggraph@1.0.2:", type=("build", "run"))
	depends_on("r-tidygraph@1.1.2:", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-textstem", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-ggwordcloud@0.5:", type=("build", "run"))
	depends_on("r-tidyfst", type=("build", "run"))
