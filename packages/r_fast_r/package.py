# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastR(RPackage):
	"""Analyze and Visualize FAST-Generated Data

	R 'shiny' app to perform data analysis and visualization for the
    Fully Automated Senescence Test (FAST) workflow.
	"""
	
	homepage = "https://f-neri.github.io/FAST.R/"
	cran = "FAST.R" 

	version("0.2.1", md5="7b44ab7e707b9e43db147d20a67af809")
	version("0.1.3", md5="cdfa376e1eab8b7c4699cef34f130ce8")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plater", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
