# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbm(RPackage):
	"""Generalized Boosted Regression Models.

	An implementation of extensions to Freund and Schapire's AdaBoost algorithm
	and Friedman's gradient boosting machine. Includes regression methods for
	least squares, absolute loss, t-distribution loss, quantile regression,
	logistic, multinomial logistic, Poisson, Cox proportional hazards  partial
	likelihood, AdaBoost exponential loss, Huberized hinge loss, and  Learning
	to Rank measures (LambdaMart). Originally developed by Greg Ridgeway."""

	cran = "gbm"

	license("GPL-2.0-or-later OR custom")

	version("2.1.9", md5="5c4da29542ad19ad41d0d6685d7c75c9")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
