# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCqrreg(RPackage):
	"""Quantile, Composite Quantile Regression and Regularized Versions

	Estimate quantile regression(QR) and composite quantile regression (cqr) and with adaptive lasso penalty using interior point (IP), majorize and minimize(MM), coordinate descent (CD), and alternating direction method of multipliers algorithms(ADMM).
	"""
	
	cran = "cqrReg" 

	version("1.2.1", md5="75504bd73c6946caa5b5d594fdf881be")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
