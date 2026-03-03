# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenogeographer(RPackage):
	"""Methods for Analysing Forensic Ancestry Informative Markers

	Evaluates likelihood ratio tests for alleged ancestry. Implements the methods of Tvedebrink et al (2018) <doi:10.1016/j.tpb.2017.12.004>.
	"""
	
	cran = "genogeographer" 

	version("0.1.19", md5="47c3c9fbe86d010ca692c7187d15f0f5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
