# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnnshiny(RPackage):
	"""Interactive Document for Working with KNN Analysis

	An interactive document on  the topic of K-nearest neighbour (KNN) using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://kartikeyabolar.shinyapps.io/KNNShiny/>.
	"""
	
	cran = "KNNShiny" 

	version("0.1.0", md5="1b3f60609374673064c9dd2dec7ef469")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-psycho", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
