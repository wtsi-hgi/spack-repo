# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrappedtools(RPackage):
	"""Useful Wrappers Around Commonly Used Functions

	The main functionalities of 'wrappedtools' are:
    adding backticks to variable names; rounding to desired precision 
    with special case for p-values; 
    selecting columns based on pattern and storing their position, name, 
    and backticked name; computing and formatting of descriptive statistics 
    (e.g. mean±SD), comparing groups and creating publication-ready tables with 
    descriptive statistics and p-values; creating specialized plots for 
    correlation matrices. Functions were mainly written for my own daily work or 
    teaching, but may be of use to others as well.
	"""
	
	cran = "wrappedtools" 

	version("0.9.3", md5="7867034efb101938d46a41efdc178a4f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
