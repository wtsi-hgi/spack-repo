# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimatr(RPackage):
	"""Fast Estimators for Design-Based Inference

	Fast procedures for small set of commonly-used, design-appropriate estimators with robust standard errors and confidence intervals. Includes estimators for linear regression, instrumental variables regression, difference-in-means, Horvitz-Thompson estimation, and regression improving precision of experimental estimates by interacting treatment with centered pre-treatment covariates introduced by Lin (2013) <doi:10.1214/12-AOAS583>.
	"""
	
	homepage = "https://declaredesign.org/r/estimatr/"
	cran = "estimatr" 

	version("1.0.2", md5="0dadaa803a54e5c38c52eb478633e89f")
	version("1.0.4", md5="264f2083ef881bd2a4ca7a5c5ac62420")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
