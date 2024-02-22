# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBestsdp(RPackage):
	"""Burden Estimate of Common Communicable Diseases in Settlements
of Displaced Populations

	Provides a practical tool for estimating the burden of common communicable diseases in settlements of displaced populations. An online version of the tool can be found at <http://who-refugee-bod.ecdf.ed.ac.uk/shiny/app/>. Estimates of burden of disease aim to synthesize data about cause-specific morbidity and mortality through a systematic approach that enables evidence-based decisions and comparisons across settings. The focus of this tool is on four acute communicable diseases and syndromes, including Acute respiratory infections, Acute diarrheal diseases, Acute jaundice syndrome and Acute febrile illnesses.
	"""
	
	cran = "bestSDP" 

	version("0.1.2", md5="7741991a7c460c22292d02440afe2e66")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
