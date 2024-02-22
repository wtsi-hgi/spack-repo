# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbshiny3(RPackage):
	"""Interactive Document for Working with Naive Bayes Classification

	An interactive document on  the topic of naive Bayes classification  analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://kartikeyab.shinyapps.io/NBShiny/>.
	"""
	
	cran = "NBShiny3" 

	version("0.1.0", md5="10091ff328daab7d74586ed8a1e9581c", url="https://cran.r-project.org/src/contrib/NBShiny3_0.1.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
