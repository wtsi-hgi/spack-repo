# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoader(RPackage):
	"""Load Data for Analysis System

	Provides a framework to load text and excel files through a 'shiny' graphical interface. It allows renaming, transforming, ordering and removing variables. It includes basic exploratory methods such as the mean, median, mode, normality test, histogram and correlation.
	"""
	
	homepage = "https://promidat.website"
	cran = "loadeR" 

	version("1.1.8", md5="4a40673e4d953922e1797182f2f64e32")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-echarts4r", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-shinydashboardplus@2:", type=("build", "run"))
