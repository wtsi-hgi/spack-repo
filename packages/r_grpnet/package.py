# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpnet(RPackage):
	"""Group Elastic Net Regularized GLMs and GAMs

	Efficient algorithms for fitting generalized linear and additive models with group elastic net penalties. Implements group lasso, group MCP, and group SCAD with an optional group ridge penalty. Computes the regularization path for linear regression (gaussian), logistic regression (binomial), multinomial logistic regression (multinomial), log-linear count regression (poisson and negative.binomial), and log-linear continuous regression (gamma and inverse gaussian). Supports default and formula methods for model specification, k-fold cross-validation for tuning the regularization parameters, and nonparametric regression via tensor product reproducing kernel (smoothing spline) basis function expansion. 
	"""
	
	cran = "grpnet" 

	version("0.3", md5="cbf2a5558b851562ad8957a7ef09caf3")

	depends_on("r@3.5:", type=("build", "run"))
