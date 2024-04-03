# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicroeco(RPackage):
	"""Microbial Community Ecology Data Analysis

	A series of statistical and plotting approaches in microbial community ecology based on the R6 class. The classes are designed for data preprocessing, taxa abundance plotting, alpha diversity analysis, beta diversity analysis, differential abundance test, null model analysis, network analysis, machine learning, environmental data analysis and functional analysis.
	"""
	
	homepage = "https://github.com/ChiLiubio/microeco"
	cran = "microeco" 

	version("1.6.0", md5="b9ce1fcb2ae6e9926aaf5a6f3e324c36")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
