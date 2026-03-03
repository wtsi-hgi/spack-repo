# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCapo4sim(RPackage):
	"""A Virtual Patient Simulator in the Context of Calcium and
Phosphate Homeostasis

	Explore calcium (Ca) and phosphate (Pi) homeostasis with two novel 'Shiny' apps, 
    building upon on a previously published mathematical model written in C, 
    to ensure efficient computations. The underlying model is accessible
    here <https://pubmed.ncbi.nlm.nih.gov/28747359/)>.
    The first application explores the fundamentals of Ca-Pi homeostasis, 
    while the second provides interactive case studies for in-depth exploration of the topic, 
    thereby seeking to foster student engagement and an integrative understanding of Ca-Pi regulation. 
    These applications are hosted at <https://rinterface.com/AppsPhysiol.html>.
	"""
	
	cran = "CaPO4Sim" 

	version("0.2.0", md5="35fec6c294fe4fa3c46f5b36f2a6c3f0")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
