# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterca(RPackage):
	"""Multiple Correspondence Analysis Based on Interpretive
Coordinates

	Various functions and a Shiny app to enrich the results of Multiple Correspondence Analysis with interpretive axes and planes (see Moschidis, Markos, and Thanopoulos, 2022; <doi:10.1108/ACI-07-2022-0191>). 
	"""
	
	cran = "interca" 

	version("0.1.2", md5="dc2143d4c98d519a259c9d270ed7335d")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
