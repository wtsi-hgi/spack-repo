# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatsomat(RPackage):
	"""Shiny Apps for Automated Data Analysis and Automated
Interpretation

	Shiny apps for automated data analysis, annotated outputs and human-readable interpretation in natural language. Designed especially for learners and applied researchers. Currently available methods: EDA, EDA with Python, Correlation Analysis, Principal Components Analysis, Confirmatory Factor Analysis.  
	"""
	
	homepage = "https://statsomat.com"
	cran = "Statsomat" 

	version("1.1.0", md5="996f24a84a8c6a84bbca445ec0cfd8c2")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shinydisconnect", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ddoutlier", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
