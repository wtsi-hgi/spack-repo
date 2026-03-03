# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratifiedrf(RPackage):
	"""Builds Trees by Sampling Variables in Groups

	Random Forest-like tree ensemble that works with groups of predictor variables. When building a tree, a number of variables is taken randomly from each group separately, thus ensuring that it considers variables from each group for the splits. Useful when rows contain information about different things (e.g. user information and product information) and it's not sensible to make a prediction with information from only one group of variables, or when there are far more variables from one group than the other and it's desired to have groups appear evenly on trees.
    Trees are grown using the C5.0 algorithm rather than the usual CART algorithm. Supports parallelization (multithreaded), missing values in predictors, and categorical variables (without doing One-Hot encoding in the processing). Can also be used to create a regular (non-stratified) Random Forest-like model, but made up of C5.0 trees and with some additional control options.
    As it's built with C5.0 trees, it works only for classification (not for regression).
	"""
	
	cran = "StratifiedRF" 

	version("0.2.2", md5="5d4c8bfd8bc890f8f2d4e7fd3cbca179")

	depends_on("r-c50", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
