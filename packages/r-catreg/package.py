# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatreg(RPackage):
	"""Solution Paths for Linear and Logistic Regression Models with
Categorical Predictors, with SCOPE Penalty

	Computes solutions for linear and logistic regression models with potentially high-dimensional categorical predictors. This is done by applying a nonconvex penalty (SCOPE) and computing solutions in an efficient path-wise fashion. The scaling of the solution paths is selected automatically. Includes functionality for selecting tuning parameter lambda by k-fold cross-validation and early termination based on information criteria. Solutions are computed by cyclical block-coordinate descent, iterating an innovative dynamic programming algorithm to compute exact solutions for each block.
	"""
	
	cran = "CatReg" 

	version("2.0.3", md5="79bfe980e943ba3b4218eff53e58f04a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
