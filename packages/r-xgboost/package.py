# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RXgboost(RPackage):
	"""Extreme Gradient Boosting.

	Extreme Gradient Boosting, which is an efficient implementation of gradient
	boosting framework. This package is its R interface. The package includes
	efficient linear model solver and tree learning algorithms. The package can
	automatically do parallel computation on a single machine which could be
	more than 10 times faster than existing gradient boosting packages. It
	supports various objective functions, including regression, classification
	and ranking. The package is made to be extensible, so that users are also
	allowed to define their own objectives easily."""

	cran = "xgboost"

	version("1.7.7.1", md5="476b159d54e363c37e7f14aa34bfc01d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix@1.1.0:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
