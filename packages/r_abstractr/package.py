# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbstractr(RPackage):
	"""An R-Shiny Application for Creating Visual Abstracts

	An R-Shiny application to create visual abstracts for original research. A variety of user defined options and formatting are included.
	"""
	
	homepage = "https://matt-kumar.shinyapps.io/portfolio"
	cran = "abstractr" 

	version("0.1.0", md5="696a9da933b8bc0bb4c93bedc2aa876b")

	depends_on("r-shiny@1.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-emojifont", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
