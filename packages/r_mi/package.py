# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMi(RPackage):
	"""Missing Data Imputation and Model Checking

	The mi package provides functions for data manipulation, imputing missing values in an approximate Bayesian framework, diagnostics of the models used to generate the imputations, confidence-building mechanisms to validate some of the assumptions of the imputation algorithm, and functions to analyze multiply imputed data sets with the appropriate degree of sampling uncertainty.
	"""
	
	homepage = "http://www.stat.columbia.edu/~gelman/"
	cran = "mi" 

	version("1.1", md5="b1823e3198ff89da48b02cf4a47d22f6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-arm@1.4.11:", type=("build", "run"))
