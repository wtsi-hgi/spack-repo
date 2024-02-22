# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArplmec(RPackage):
	"""Censored Mixed-Effects Models with Different Correlation
Structures

	Left, right or interval censored mixed-effects linear model with autoregressive errors of order p or DEC correlation structure using the type-EM algorithm. The error distribution  can be Normal or t-Student. It provides the  parameter estimates, the standard errors  and prediction of future observations (available only for the normal case). Olivari et all (2021) <doi:10.1080/10543406.2020.1852246>.
	"""
	
	cran = "ARpLMEC" 

	version("2.4.1", md5="e9f1169e1d0db1336cb5658ab888e757")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-relliptical", type=("build", "run"))
	depends_on("r-truncatednormal", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
