# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmnet(RPackage):
	"""Lasso and Elastic-Net Regularized Generalized Linear Models.

	Extremely efficient procedures for fitting the entire lasso or elastic-net
	regularization path for linear regression, logistic and multinomial
	regression models, Poisson regression and the Cox model. Two recent
	additions are the multiple-response Gaussian, and the grouped multinomial.
	The algorithm uses cyclical coordinate descent in a path-wise fashion, as
	described in the paper linked to via the URL below."""

	cran = "glmnet"

	license("GPL-2.0-only")

	version("4.1-8", md5="98a316b4857ea3f46b44285dc5764068")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.0.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
