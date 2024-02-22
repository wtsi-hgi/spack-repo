# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForesterror(RPackage):
	"""A Unified Framework for Random Forest Prediction Error
Estimation

	Estimates the conditional error distributions of random forest
    predictions and common parameters of those distributions, including
    conditional misclassification rates, conditional mean squared prediction
    errors, conditional biases, and conditional quantiles, by out-of-bag
    weighting of out-of-bag prediction errors as proposed by Lu and Hardin
    (2021). This package is compatible with several existing packages that
    implement random forests in R.
	"""
	
	cran = "forestError" 

	version("1.1.0", md5="8c8a75df0ca254169d83f9c780885740")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
