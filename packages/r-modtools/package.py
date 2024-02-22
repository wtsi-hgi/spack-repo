# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModtools(RPackage):
	"""Tools for Building Regression and Classification Models

	Collection of tools for regression and classification tasks. The package implements a consistent user interface to the most popular regression and classification algorithms, such as random forest, neural networks, C5 trees and support vector machines, and complements it with a handful of auxiliary functions, such as variable importance and a tuning function for the parameters.
	"""
	
	cran = "ModTools" 

	version("0.9.6", md5="446aea9a444d414c07913f3061fc7f91")

	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-relaimpo", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-neuralnettools", type=("build", "run"))
	depends_on("r-naivebayes", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
