# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtlasso(RPackage):
	"""Maximum Penalized Likelihood Estimation with Extended Lasso
Penalty

	Estimates coefficients of extended LASSO penalized linear regression and generalized linear models. Currently lasso and elastic net penalized linear regression and generalized linear models are considered. This package currently utilizes an accurate approximation of L1 penalty and then a modified Jacobi algorithm to estimate the coefficients. There is provision for plotting of the solutions and predictions of coefficients at given values of lambda. This package also contains functions for cross validation to select a suitable lambda value given the data. Also provides a function for estimation in fused lasso penalized linear regression. For more details, see Mandal, B. N.(2014). Computational methods for L1 penalized GLM model fitting, unpublished report submitted to Macquarie University, NSW, Australia.
	"""
	
	cran = "extlasso" 

	version("0.3", md5="9fef24dfa177812ae197123d7d4cb7be")

	depends_on("r@3.1.1:", type=("build", "run"))
