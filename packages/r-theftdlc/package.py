# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTheftdlc(RPackage):
	"""Analyse and Interpret Time Series Features

	Provides a suite of functions for analysing, interpreting, and visualising
    time-series features calculated from different feature sets from the 'theft' package. 
    Implements statistical learning methodologies described in Henderson, T., 
    Bryant, A., and Fulcher, B. (2023) <arXiv:2303.17809>.
	"""
	
	homepage = "https://hendersontrent.github.io/theftdlc/"
	cran = "theftdlc" 

	version("0.1.0", md5="f9cc6f372405da9f93e822302f18e5be")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-theft@0.6.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-normaliser", type=("build", "run"))
	depends_on("r-correctr", type=("build", "run"))
