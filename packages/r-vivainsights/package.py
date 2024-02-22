# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVivainsights(RPackage):
	"""Analyze and Visualize Data from 'Microsoft Viva Insights'

	Provides a versatile range of functions, including exploratory data analysis, time-series analysis, organizational network analysis, and data validation, whilst at the same time implements a set of best practices in analyzing and visualizing data specific to 'Microsoft Viva Insights'.
	"""
	
	homepage = "https://microsoft.github.io/vivainsights/"
	cran = "vivainsights" 

	version("0.5.1", md5="22d0ab77615e56cfa085060216b3193d")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-wpa", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
