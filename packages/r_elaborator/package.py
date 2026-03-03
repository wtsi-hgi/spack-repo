# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElaborator(RPackage):
	"""A 'shiny' Application for Exploring Laboratory Data

	A novel concept for generating knowledge and gaining insights into laboratory data. You will be able to efficiently and easily explore your laboratory data from different perspectives.
	"""
	
	cran = "elaborator" 

	version("1.1", md5="fb733c3cb7e0e5a6e7de9fd97dd37c5e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
