# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnlasso(RPackage):
	"""Non-Negative Lasso and Elastic Net Penalized Generalized Linear
Models

	Estimates of coefficients of lasso penalized linear regression and generalized linear models subject to non-negativity constraints on the parameters using multiplicative iterative algorithm. Entire regularization path for a sequence of lambda values can be obtained. Functions are available for creating plots of regularization path, cross validation and estimating coefficients at a given lambda value. There is also provision for obtaining standard error of coefficient estimates.
	"""
	
	cran = "nnlasso" 

	version("0.3", md5="e450efa4bc9b9ca55fb60e8f4ba6d5de")

	depends_on("r@3.2.2:", type=("build", "run"))
