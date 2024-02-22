# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFftrees(RPackage):
	"""Generate, Visualise, and Evaluate Fast-and-Frugal Decision Trees

	Create, visualize, and test fast-and-frugal decision trees (FFTs) using the algorithms and methods described by Phillips, Neth, Woike & Gaissmaier (2017), <doi:10.1017/S1930297500006239>. 
    FFTs are simple and transparent decision trees for solving binary classification problems. 
    FFTs can be preferable to more complex algorithms because they require very little information, are easy to understand and communicate, and are robust against overfitting.
	"""
	
	homepage = "https://CRAN.R-project.org/package=FFTrees"
	cran = "FFTrees" 

	version("2.0.0", md5="31c2fe9cea43419b489b8aad8d4fe460")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
