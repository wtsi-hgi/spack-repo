# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmshiny(RPackage):
	"""Interactive Document for Working with Confusion Matrix

	An interactive document on  the topic of confusion matrix analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at <https://predanalyticssessions1.shinyapps.io/ConfusionMatrixShiny/>.
	"""
	
	cran = "CMShiny" 

	version("0.1.0", md5="78799e2845f5ae447578dcbd96b53a70")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
