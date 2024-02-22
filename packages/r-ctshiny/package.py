# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtshiny(RPackage):
	"""Interactive Document for Working with Classification Tree
Analysis

	An interactive document on  the topic of classification tree analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://kartikeyab.shinyapps.io/CTShiny/>.
	"""
	
	cran = "CTShiny" 

	version("0.1.0", md5="b9b6524a9a7335b6f6cd3a5e17c74ad1")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
