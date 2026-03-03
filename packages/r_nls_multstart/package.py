# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlsMultstart(RPackage):
	"""Robust Non-Linear Regression using AIC Scores

	Non-linear least squares regression with the Levenberg-Marquardt algorithm using multiple starting values for increasing the chance that the minimum found is the global minimum.
	"""
	
	cran = "nls.multstart" 

	version("1.3.0", md5="b7b7a4ba562807b1f51c821e37fe1751")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
