# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatman(RPackage):
	"""Material Management

	A set of functions, classes and methods for performing ABC and ABC/XYZ analyses, identifying overperforming, underperforming and constantly performing items, and plotting, analyzing as well as predicting the temporal development of items.
	"""
	
	cran = "matman" 

	version("1.1.3", md5="18cdea5b519e63d5f13ed2359dbe1642")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
