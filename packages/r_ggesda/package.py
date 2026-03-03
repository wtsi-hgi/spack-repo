# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgesda(RPackage):
	"""Exploratory Symbolic Data Analysis with 'ggplot2'

	Implements an extension of 'ggplot2' and visualizes the symbolic data with multiple plot which can be adjusted by more general and flexible input arguments. It also provides a function to transform the classical data to symbolic data by both clustering algorithm and customized method.
	"""
	
	homepage = "https://github.com/kiangkiangkiang/ggESDA"
	cran = "ggESDA" 

	version("0.2.0", md5="9d3d9b6c2950e6b4b905e7bbfa73a751")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-rsda", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
