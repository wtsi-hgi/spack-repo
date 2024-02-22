# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonlinearrdd(RPackage):
	"""Nonlinear Regression Discontinuity Design

	Estimation of the possibly nonlinear and non separable structural function in regression discontinuity designs with a continuous treatment variable. The method is based on Xie (2022) <arXiv:2204.08168>.
	"""
	
	cran = "NonlinearRDD" 

	version("0.0.4", md5="8e4a70d296d16568d64e8b488a068395")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rdrobust", type=("build", "run"))
	depends_on("r-rddensity", type=("build", "run"))
	depends_on("r-lpdensity", type=("build", "run"))
	depends_on("r-lpcde", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
