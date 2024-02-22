# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReviewr(RPackage):
	"""A Light-Weight, Portable Tool for Reviewing Individual Patient
Records

	A portable Shiny tool to explore patient-level electronic health record data 
    and perform chart review in a single integrated framework. This tool supports 
    browsing clinical data in many different formats including multiple versions 
    of the 'OMOP' common data model as well as the 'MIMIC-III' data model. In 
    addition, chart review information is captured and stored securely via the 
    Shiny interface in a 'REDCap' (Research Electronic Data Capture) project 
    using the 'REDCap' API. See the 'ReviewR' website for additional information, 
    documentation, and examples.
	"""
	
	homepage = "https://reviewr.thewileylab.org/"
	cran = "ReviewR" 

	version("2.3.10", md5="3ef17fbd2c1892623ff2f2fd24424051")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bigrquery@1.2:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-gargle", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-redcapapi", type=("build", "run"))
	depends_on("r-redcapr", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinycssloaders@1:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus@2:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets@0.6:", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
