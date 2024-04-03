# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestgardener(RPackage):
	"""Information Analysis for Test and Rating Scale Data

	Develop, evaluate, and score multiple choice examinations, 
 psychological scales, questionnaires, and similar types of data involving
 sequences of choices among one or more sets of answers.
 This version of the package should be considered as brand new.  Almost all
 of the functions have been changed, including their argument list.
 See the file NEWS.Rd in the Inst folder for more information.
 Using the package does not require any formal statistical knowledge 
 beyond what would be provided by a first course in statistics in a 
 social science department.  There the user would encounter the concept 
 of probability and how it is used to model data and make decisions, 
 and would become familiar with basic mathematical and statistical notation.
 Most of the output is in graphical form. 
	"""
	
	cran = "TestGardener" 

	version("3.3.3", md5="c6477e984380da5aad8a6148fbc23ab7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
