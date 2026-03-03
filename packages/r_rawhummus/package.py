# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRawhummus(RPackage):
	"""Raw Data Quality Control Tool for LC-MS System

	Assess LC–MS system performance by visualizing instrument log
    files and monitoring raw quality control samples within a project.
	"""
	
	cran = "RawHummus" 

	version("0.3.3", md5="a98b406bada96a44dfefb75aee849761")

	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.5.9001:", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rams", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
