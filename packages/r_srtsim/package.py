# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrtsim(RPackage):
	"""Simulator for Spatially Resolved Transcriptomics

	An independent, reproducible, and flexible Spatially Resolved Transcriptomics (SRT) simulation framework that can be used to facilitate the development of SRT analytical methods for a wide variety of SRT-specific analyses. It utilizes spatial localization information to simulate SRT expression count data in a reproducible and scalable fashion. Two major simulation schemes are implemented in 'SRTsim': reference-based and reference-free.
	"""
	
	cran = "SRTsim" 

	version("0.99.6", md5="cbb3a160221ca94d06d844420a5c5ffc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dashboardthemes", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
