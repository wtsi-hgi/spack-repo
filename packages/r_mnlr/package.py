# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnlr(RPackage):
	"""Interactive Shiny Presentation for Working with Multinomial
Logistic Regression

	An interactive presentation on  the topic of Multinomial Logistic Regression. It is helpful to those who want to learn Multinomial Logistic Regression quickly and get a hands on experience. The presentation has a template for solving problems on Multinomial Logistic Regression. Runtime examples are provided in the package function as well as at  <https://jarvisatharva.shinyapps.io/MultinomPresentation>. 
	"""
	
	cran = "MNLR" 

	version("0.1.0", md5="e625e4c72a172398eb7ffc220d0ea9af")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
