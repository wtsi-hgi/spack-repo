# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebr(RPackage):
	"""Data and Functions for Web-Based Analysis

	Several analysis-related functions for the book entitled
    "Web-based Analysis without R in Your Computer"(written in Korean, ISBN 978-89-5566-185-9)
    by Keon-Woong Moon. The main function plot.htest() shows the distribution of statistic for
    the object of class 'htest'.
	"""
	
	homepage = "https://github.com/cardiomoon/webr"
	cran = "webr" 

	version("0.1.5", md5="293e077a4613adff332dc0cebfad2165")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-moonbook", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rrtable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-ztable", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
