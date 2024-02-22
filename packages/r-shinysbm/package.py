# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinysbm(RPackage):
	"""'shiny' Application to Use the Stochastic Block Model

	A 'shiny' interface for a simpler use of the 'sbm' R package. 
    It also contains useful functions to easily explore the 'sbm' package results. 
    With this package you should be able to use the stochastic block model 
    without any knowledge in R, get automatic reports and nice visuals, as 
    well as learning the basic functions of 'sbm'.
	"""
	
	cran = "shinySbm" 

	version("0.1.5", md5="288a8336bbb29f592445cbe994398ea7")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-sbm", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-fresh", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
