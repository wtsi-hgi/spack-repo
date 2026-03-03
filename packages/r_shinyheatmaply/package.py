# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyheatmaply(RPackage):
	"""Deploy 'heatmaply' using 'shiny'

	Access functionality of the 'heatmaply' package through 'Shiny UI'.
	"""
	
	homepage = "https://github.com/yonicd/shinyHeatmaply"
	cran = "shinyHeatmaply" 

	version("0.2.0", md5="91b76c9e73afea56239f51332d123809")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-heatmaply@1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
