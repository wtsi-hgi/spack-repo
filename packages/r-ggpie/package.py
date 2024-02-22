# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpie(RPackage):
	"""Pie, Donut and Rose Pie Plots

	Create pie, donut and rose pie plot with 'ggplot2'. 
	"""
	
	homepage = "https://github.com/showteeth/ggpie"
	cran = "ggpie" 

	version("0.2.5", md5="02cf1b3fe70a94e343140e0520d1258a")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
