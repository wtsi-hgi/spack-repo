# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarsurv(RPackage):
	"""Correlation-Adjusted Regression Survival (CARS) Scores

	Contains functions to estimate the Correlation-Adjusted Regression Survival (CARS) Scores. The method is described in Welchowski, T. and Zuber, V. and Schmid, M., (2018), Correlation-Adjusted Regression Survival Scores for High-Dimensional Variable Selection, <arXiv:1802.08178>.
	"""
	
	cran = "carSurv" 

	version("1.0.0", md5="2bcd654cb1bbbeccb77b6754ea85066d")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
