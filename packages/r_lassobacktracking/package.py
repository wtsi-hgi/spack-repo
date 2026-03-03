# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLassobacktracking(RPackage):
	"""Modelling Interactions in High-Dimensional Data with
Backtracking

	Implementation of the algorithm introduced in Shah, R. D.
    (2016) <https://www.jmlr.org/papers/volume17/13-515/13-515.pdf>.
    Data with thousands of predictors can be handled. The algorithm
    performs sequential Lasso fits on design matrices containing
    increasing sets of candidate interactions. Previous fits are used to greatly
    speed up subsequent fits, so the algorithm is very efficient.
	"""
	
	homepage = "https://www.jmlr.org/papers/volume17/13-515/13-515.pdf"
	cran = "LassoBacktracking" 

	version("1.1", md5="c36358df2456f7ef89cec1daa9136b6f")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
