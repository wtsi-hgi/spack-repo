# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimaa(RPackage):
	"""Nominal Data Mining Analysis

	Functions for nominal data mining based on bipartite graphs, which build a pipeline for analysis and missing values imputation. Methods are mainly from the paper: Jafari, Mohieddin, et al. (2021) <doi:10.1101/2021.03.18.436040>, some new ones are also included.
	"""
	
	homepage = "https://github.com/jafarilab/NIMAA"
	cran = "NIMAA" 

	version("0.2.1", md5="1675d06b07eac30b2bb8eceb0b7a6d58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-skimr", type=("build", "run"))
	depends_on("r-bnstruct", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-missmda", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
