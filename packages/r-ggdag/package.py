# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdag(RPackage):
	"""Analyze and Create Elegant Directed Acyclic Graphs

	Tidy, analyze, and plot directed acyclic graphs (DAGs).
    'ggdag' is built on top of 'dagitty', an R package that uses the
    'DAGitty' web tool (<https://dagitty.net/>) for creating and analyzing
    DAGs. 'ggdag' makes it easy to tidy and plot 'dagitty' objects using
    'ggplot2' and 'ggraph', as well as common analytic and graphical
    functions, such as determining adjustment sets and node relationships.
	"""
	
	homepage = "https://github.com/r-causal/ggdag"
	cran = "ggdag" 

	version("0.2.12", md5="3a31ea904a20ce3591e83f4b855a394e")
	version("0.2.11", md5="32f6a5558bc50e7be9c5d18f4a7be8d6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dagitty", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggraph@2:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
