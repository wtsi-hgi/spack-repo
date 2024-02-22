# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConquer(RPackage):
	"""Convolution-Type Smoothed Quantile Regression.

	Fast and accurate convolution-type smoothed quantile regression.
	Implemented using Barzilai-Borwein gradient descent with a Huber regression
	warm start. Construct confidence intervals for regression coefficients
	using multiplier bootstrap."""

	cran = "conquer"

	version("1.3.3", md5="d1b977a1c7d6bf86e4092273ab496b15")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.850.1:", type=("build", "run"))
