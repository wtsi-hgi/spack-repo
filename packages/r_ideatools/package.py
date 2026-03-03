# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdeatools(RPackage):
	"""Individual and Group Farm Sustainability Assessments using the
IDEA4 Method

	Collection of tools to automate the processing of data collected though the IDEA4 method (see Zahm et al. (2018) <doi:10.1051/cagri/2019004> ). Starting from the original data collecting files this packages provides functions to compute IDEA indicators, draw modern and aesthetic plots, and produce a wide range of reporting materials. 
	"""
	
	homepage = "https://davidcarayon.github.io/IDEATools/index.html"
	cran = "IDEATools" 

	version("3.5.2", md5="2cfe1875822d21b7f97d9749aaf839f6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
