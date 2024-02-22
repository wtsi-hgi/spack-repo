# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtshiny2(RPackage):
	"""Interactive Document for Working with Classification Tree
Analysis

	An interactive document on  the topic of classification tree analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://kartikeyab.shinyapps.io/CTShiny/>.
	"""
	
	cran = "CTShiny2" 

	version("0.1.0", md5="dc4e01501bca95cbf94ace284b6ddc76", url="https://cran.r-project.org/src/contrib/CTShiny2_0.1.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
