# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSodavis(RPackage):
	"""SODA: Main and Interaction Effects Selection for Logistic
Regression, Quadratic Discriminant and General Index Models

	Variable and interaction selection are essential to classification in high-dimensional setting. In this package, we provide the implementation of SODA procedure, which is a forward-backward algorithm that selects both main and interaction effects under logistic regression and quadratic discriminant analysis. We also provide an extension, S-SODA, for dealing with the variable selection problem for semi-parametric models with continuous responses.
	"""
	
	cran = "sodavis" 

	version("1.2", md5="b03479e63890b6835965a295134d0d99")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
