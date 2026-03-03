# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinylink(RPackage):
	"""'Shiny' Based Record Linkage Tool

	A bridge is created between existing robust open-source record linkage algorithms and an urgently needed user-friendly platform that removes financial and technical barriers, setting a new standard for data interoperability in public health and bioinformatics. The 'fastLink' algorithms are used for matching. Ted Enamorado et al. (2019) <doi:10.1017/S0003055418000783>.
	"""
	
	cran = "ShinyLink" 

	version("0.2.2", md5="0efdbf43d2793515956f546f5d684caf")

	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-dt@0.25:", type=("build", "run"))
	depends_on("r-fastlink", type=("build", "run"))
	depends_on("r-gender", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggvenn", type=("build", "run"))
	depends_on("r-golem@0.3.5:", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
