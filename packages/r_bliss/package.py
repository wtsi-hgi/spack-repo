# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBliss(RPackage):
	"""Bayesian Functional Linear Regression with Sparse Step Functions

	A method for the Bayesian functional linear regression model (scalar-on-function),
  including two estimators of the coefficient function and an estimator of its support.
  A representation of the posterior distribution is also available. Grollemund P-M., Abraham C., 
  Baragatti M., Pudlo P. (2019) <doi:10.1214/18-BA1095>.
	"""
	
	homepage = "https://github.com/pmgrollemund/bliss"
	cran = "bliss" 

	version("1.0.4", md5="ae46102ac99487add1a94c0e3e37881e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
