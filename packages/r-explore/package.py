# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExplore(RPackage):
	"""Simplifies Exploratory Data Analysis

	Interactive data exploration with one line of code, automated
    reporting or use an easy to remember set of tidy functions for low
    code exploratory data analysis.
	"""
	
	homepage = "https://rolkra.github.io/explore/"
	cran = "explore" 

	version("1.1.1", md5="feb4ab75a4486d71ac8bb9a291ed458d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-dt@0.3:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-palmerpenguins", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
