# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlearning(RPackage):
	"""Machine Learning Algorithms with Unified Interface and Confusion
Matrices

	A unified interface is provided to various machine learning
  algorithms like linear or quadratic discriminant analysis, k-nearest
  neighbors, random forest, support vector machine, ... It allows to train,
  test, and apply cross-validation using similar functions and function
  arguments with a minimalist and clean, formula-based interface. Missing data
  are processed the same way as base and stats R functions for all algorithms,
  both in training and testing. Confusion matrices are also provided with a rich
  set of metrics calculated and a few specific plots.
	"""
	
	homepage = "https://www.sciviews.org/mlearning/"
	cran = "mlearning" 

	version("1.2.1", md5="a513705154f2027d7b528f9cf83d204a")

	depends_on("r@3.0.4:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
