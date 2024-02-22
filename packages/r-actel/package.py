# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActel(RPackage):
	"""Acoustic Telemetry Data Analysis

	Designed for studies where animals tagged with acoustic tags are expected
    to move through receiver arrays. This package combines the advantages of automatic sorting and checking 
    of animal movements with the possibility for user intervention on tags that deviate from expected 
    behaviour. The three analysis functions (explore(), migration() and residency()) 
    allow the users to analyse their data in a systematic way, making it easy to compare results from 
    different studies.
    CJS calculations are based on Perry et al. (2012) <https://www.researchgate.net/publication/256443823_Using_mark-recapture_models_to_estimate_survival_from_telemetry_data>.
	"""
	
	homepage = "https://github.com/hugomflavio/actel"
	cran = "actel" 

	version("1.3.0", md5="6aabeb46f304d7fdade48849d544f1ae")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-diagrammersvg", type=("build", "run"))
	depends_on("r-fasttime", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
