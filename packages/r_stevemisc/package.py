# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStevemisc(RPackage):
	"""Steve's Miscellaneous Functions

	These are miscellaneous functions that I find useful for my research and teaching.
    The contents include themes for plots, functions for simulating
    quantities of interest from regression models, functions for simulating various 
    forms of fake data for instructional/research purposes, and many more. All told, the functions
    provided here are broadly useful for data organization, data presentation, data recoding, 
    and data simulation. 
	"""
	
	cran = "stevemisc" 

	version("1.7.0", md5="1c8cef27b0b454e61bf0e6654f538b15")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
