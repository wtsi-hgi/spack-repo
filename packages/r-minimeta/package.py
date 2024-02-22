# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinimeta(RPackage):
	"""Web Application to Run Meta-Analyses

	Shiny web application to run meta-analyses. 
    Essentially a graphical front-end to package 'meta' for R. 
    Can be useful as an educational tool, and for quickly 
    analyzing and sharing meta-analyses. 
    Provides output to quickly fill in GRADE (Grading of 
    Recommendations, Assessment, Development and Evaluations)
    Summary-of-Findings tables. 
    Importantly, it allows further processing of the results 
    inside R, in case more specific analyses are needed.
	"""
	
	cran = "miniMeta" 

	version("0.3.1", md5="6e7684b67bc9d593b6e25c1353442590")

	depends_on("r-meta@7.0.0:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
