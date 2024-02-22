# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrviz(RPackage):
	"""Visualise Correlations

	An investigative tool designed to help users visualize correlations between variables in their datasets. This package aims to provide an easy and effective way to explore and visualize these correlations, making it easier to interpret and communicate results.
	"""
	
	cran = "corrViz" 

	version("0.1.0", md5="86ab861790f9bed9122bf8d307138716")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dendser", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
