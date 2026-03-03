# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgflowchart(RPackage):
	"""Flowcharts with 'ggplot2'

	Flowcharts can be a useful way to visualise complex processes. This package 
    uses the layered grammar of graphics of 'ggplot2' to create simple flowcharts.
	"""
	
	homepage = "https://nrennie.github.io/ggflowchart/"
	cran = "ggflowchart" 

	version("1.0.0", md5="d7581800de67946e2a3578f0da2e9271")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
