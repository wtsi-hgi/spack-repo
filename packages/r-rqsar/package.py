# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqsar(RPackage):
	"""QSAR Modeling with Multiple Algorithms: MLR, PLS, and Random
Forest

	Quantitative Structure-Activity Relationship (QSAR) modeling is a valuable tool in computational chemistry and drug design, where it aims to predict the activity or property of chemical compounds based on their molecular structure. In this vignette, we present the 'rQSAR' package, which provides functions for variable selection and QSAR modeling using Multiple Linear Regression (MLR), Partial Least Squares (PLS), and Random Forest algorithms.
	"""
	
	cran = "rQSAR" 

	version("1.0.0", md5="14d4414716d5beb9117afc2d85b5686b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcdk@3.8.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
