# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgquickeda(RPackage):
	"""Quickly Explore Your Data Using 'ggplot2' and 'table1' Summary
Tables

	Quickly and easily perform exploratory data analysis by uploading your
     data as a 'csv' file. Start generating insights using 'ggplot2' plots and
     'table1' tables with descriptive stats, all using an easy-to-use point and click 
     'Shiny' interface.
	"""
	
	homepage = "https://github.com/smouksassi/ggquickeda"
	cran = "ggquickeda" 

	version("0.3.1", md5="ce1f98bd9e8572f7fc1d462b70edf237")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-ggally@2.1:", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-ggrepel@0.7:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny@1.0.4:", type=("build", "run"))
	depends_on("r-shinyjs@1.1:", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-table1@1.4.2:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-patchwork@1.2:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
