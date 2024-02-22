# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmicd(RPackage):
	"""Statistical Methods for Interval-Censored Data

	Functions that provide statistical methods for interval-censored (grouped) data. The package supports the estimation of linear and linear mixed regression models with interval-censored dependent variables. Parameter estimates are obtained by a stochastic expectation maximization algorithm. Furthermore, the package enables the direct (without covariates) estimation of statistical indicators from interval-censored data via an iterative kernel density algorithm. Survey and Organisation for Economic Co-operation and Development (OECD) weights can be included into the direct estimation (see, Walter, P. (2019) <doi:10.17169/refubium-1621>).
	"""
	
	cran = "smicd" 

	version("1.1.3", md5="53b9455d8ef460c508894e2f20ac3d20")

	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
