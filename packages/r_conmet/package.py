# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConmet(RPackage):
	"""Construct Measurement Evaluation Tool

	With this package you can run 'ConMET' locally in R. 'ConMET' is an R-shiny application that facilitates performing and evaluating confirmatory factor analyses (CFAs) and is useful for running and reporting typical measurement models in applied psychology and management journals. 'ConMET' automatically creates, compares and summarizes CFA models. Most common fit indices (E.g., CFI and SRMR) are put in an overview table. ConMET also allows to test for common method variance. The application is particularly useful for teaching and instruction of measurement issues in survey research. The application uses the 'lavaan' package (Rosseel, 2012) to run CFAs.
	"""
	
	cran = "conmet" 

	version("0.1.0", md5="2b5fdbfc9dbffdb789d09ce7780c9890")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-summarytools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-semtools", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
