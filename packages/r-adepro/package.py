# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdepro(RPackage):
	"""A 'shiny' Application for the (Audio-)Visualization of Adverse
Event Profiles

	Contains a 'shiny' application called AdEPro (Animation of Adverse Event Profiles) which (audio-)visualizes adverse events occurring in clinical trials. As this data is usually considered sensitive, this tool is provided as a stand-alone application that can be launched from any local machine on which the data is stored.
	"""
	
	cran = "adepro" 

	version("3.2.0", md5="4ef61cdf6eb0aea9b941c06dee51b6f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-seriation@1.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-audio", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-gclus", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
