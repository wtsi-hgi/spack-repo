# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitweetr(RPackage):
	"""Early Detection of Public Health Threats from 'Twitter' Data

	It allows you to automatically monitor trends of tweets by time, place and topic aiming at detecting public health threats early through the detection of signals (e.g. an unusual increase in the number of tweets). It was designed to focus on infectious diseases, and it can be extended to all hazards or other fields of study by modifying the topics and keywords. More information is available in the 'epitweetr' peer-review publication (doi:10.2807/1560-7917.ES.2022.27.39.2200177).
	"""
	
	homepage = "https://github.com/EU-ECDC/epitweetr"
	cran = "epitweetr" 

	version("2.2.16", md5="9b7dd39e80771b7fe1031f1316ef88e0")

	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-emayili", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rtweet", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rnaturalearthdata", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
