# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsmodule(RPackage):
	"""'RStudio' Addins and 'Shiny' Modules for Medical Research

	'RStudio' addins and 'Shiny' modules for descriptive statistics, regression and survival analysis.
	"""
	
	homepage = "https://github.com/jinseob2kim/jsmodule"
	cran = "jsmodule" 

	version("1.5.1", md5="b594bea51e36d41e690b3ad1ad1dbe32")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-jstable", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-matchit@3:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-jskm@0.4.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-maxstat", type=("build", "run"))
	depends_on("r-survidinri", type=("build", "run"))
	depends_on("r-timeroc", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-see", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-rvg", type=("build", "run"))
	depends_on("r-epidisplay", type=("build", "run"))
	depends_on("r-forestploter", type=("build", "run"))
