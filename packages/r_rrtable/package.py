# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrtable(RPackage):
	"""Reproducible Research with a Table of R Codes

	Makes documents containing plots and tables from a table of R codes. 
    Can make "HTML", "pdf('LaTex')", "docx('MS Word')" and "pptx('MS Powerpoint')" documents with or without R code.
    In the package, modularized 'shiny' app codes are provided. These modules are intended for reuse across applications.
	"""
	
	cran = "rrtable" 

	version("0.3.0", md5="dccb84c02745d1a462c7e9601478ba4b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-officer@0.4.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-flextable@0.4.4:", type=("build", "run"))
	depends_on("r-rvg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-devemf", type=("build", "run"))
	depends_on("r-moonbook@0.1.8:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-editdata", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-ztable@0.1.8:", type=("build", "run"))
