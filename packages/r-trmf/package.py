# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrmf(RPackage):
	"""Temporally Regularized Matrix Factorization

	Functions to estimate temporally regularized matrix factorizations (TRMF) for forecasting and imputing values in short but high-dimensional time series. Uses regularized alternating least squares to compute the factorization, allows for several types of constraints on matrix factors and natively handles weighted and missing data.
	"""
	
	cran = "TRMF" 

	version("0.1.5", md5="283310db26a107f6844647f3f3a9ab3a")

	depends_on("r-matrix@1.3.3:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
