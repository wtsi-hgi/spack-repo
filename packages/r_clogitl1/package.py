# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClogitl1(RPackage):
	"""Fitting Exact Conditional Logistic Regression with Lasso and
Elastic Net Penalties

	Tools for the fitting and cross validation of exact conditional logistic regression models with lasso and elastic net penalties. Uses cyclic coordinate descent and warm starts to compute the entire path efficiently.
	"""
	
	cran = "clogitL1" 

	version("1.5", md5="edb836c9c8a48077f054c724946f144f", url="https://cran.r-project.org/src/contrib/clogitL1_1.5.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
