# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogantree(RPackage):
	"""Tree-Based Models for the Analysis of Log Files from
Computer-Based Assessments

	Enables researchers to model log-file data from computer-based assessments using machine-learning techniques. It allows researchers to generate new knowledge by comparing the performance of three tree-based classification models (i.e., decision trees, random forest, and gradient boosting) to predict student's outcome. It also contains a set of handful functions for the analysis of the features' influence on the modeling. Data from the Climate control item from the 2012 Programme for International Student Assessment (PISA, <https://www.oecd.org/pisa/>) is available for an illustration of the package's capability. He, Q., & von Davier, M. (2015) <doi:10.1007/978-3-319-19977-1_13> Boehmke, B., & Greenwell, B. M. (2019) <doi:10.1201/9780367816377> .
	"""
	
	cran = "LOGANTree" 

	version("0.1.1", md5="4802a7771f05a34f7b31bf4cdf01e51d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-caretensemble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
