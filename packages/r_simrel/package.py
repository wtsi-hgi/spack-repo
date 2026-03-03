# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimrel(RPackage):
	"""Simulation of Multivariate Linear Model Data

	Researchers have been using simulated data from a multivariate linear model to compare and evaluate different methods, ideas and models. Additionally, teachers and educators have been using a simulation tool to demonstrate and teach various statistical and machine learning concepts.
    This package helps users to simulate linear model data with a wide range of properties by tuning few parameters such as relevant latent components. In addition, a shiny app as an 'RStudio' gadget gives users a simple interface for using the simulation function. See more on: Sæbø, S., Almøy, T., Helland, I.S. (2015) <doi:10.1016/j.chemolab.2015.05.012> and Rimal, R., Almøy, T., Sæbø, S. (2018) <doi:10.1016/j.chemolab.2018.02.009>.
	"""
	
	homepage = "https://simulatr.github.io/simrel/"
	cran = "simrel" 

	version("2.1.0", md5="39b8d7e8fc4951a141e44bf0c405216a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-frf2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
