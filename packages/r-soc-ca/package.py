# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSocCa(RPackage):
	"""Specific Correspondence Analysis for the Social Sciences

	Specific and class specific multiple correspondence analysis on
    survey-like data. Soc.ca is optimized to the needs of the social scientist and
    presents easily interpretable results in near publication ready quality.
	"""
	
	homepage = "https://github.com/Rsoc/soc.ca"
	cran = "soc.ca" 

	version("0.8.0", md5="675dcb64630617f7f41a62dd1fb9ae77")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmltable", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
