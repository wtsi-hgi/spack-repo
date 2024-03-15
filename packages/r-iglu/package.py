# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIglu(RPackage):
	"""Interpreting Glucose Data from Continuous Glucose Monitors

	Implements a wide range of metrics for measuring glucose control and glucose variability based on continuous glucose monitoring data. The list of implemented metrics is summarized in Rodbard (2009) <doi:10.1089/dia.2009.0015>. Additional visualization tools include time-series plots, lasagna plots and ambulatory glucose profile report. 
	"""
	
	homepage = "https://irinagain.github.io/iglu/"
	cran = "iglu" 

	version("4.0.0", md5="77d865f0b76811ac482d00582356245f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
