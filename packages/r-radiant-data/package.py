# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadiantData(RPackage):
	"""Data Menu for Radiant: Business Analytics using R and Shiny

	The Radiant Data menu includes interfaces for loading, saving,
    viewing, visualizing, summarizing, transforming, and combining data. It also
    contains functionality to generate reproducible reports of the analyses
    conducted in the application.
	"""
	
	homepage = "https://github.com/radiant-rstats/radiant.data/"
	cran = "radiant.data" 

	version("1.6.3", md5="ec3fac3727cc43558103804934e60f36")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-arrow@12.0.1:", type=("build", "run"))
	depends_on("r-broom@0.5.2:", type=("build", "run"))
	depends_on("r-car@3.0.0:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-markdown@1.7:", type=("build", "run"))
	depends_on("r-rmarkdown@2.22:", type=("build", "run"))
	depends_on("r-shiny@1.8:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-shinyace@0.4.1:", type=("build", "run"))
	depends_on("r-psych@1.8.4:", type=("build", "run"))
	depends_on("r-dt@0.28:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-readxl@1:", type=("build", "run"))
	depends_on("r-writexl@0.2:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-curl@2.5:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-import@1.1:", type=("build", "run"))
	depends_on("r-plotly@4.7.1:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-shinyfiles@0.9.1:", type=("build", "run"))
	depends_on("r-stringi@1.2.4:", type=("build", "run"))
	depends_on("r-randomizr@0.20:", type=("build", "run"))
	depends_on("r-patchwork@1:", type=("build", "run"))
	depends_on("r-bslib@0.5:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
