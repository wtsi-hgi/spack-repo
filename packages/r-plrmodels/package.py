# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlrmodels(RPackage):
	"""Statistical Inference in Partial Linear Regression Models

	Contains statistical inference tools applied to Partial Linear Regression (PLR) models. Specifically, point estimation, confidence intervals estimation, bandwidth selection, goodness-of-fit tests and analysis of covariance are considered. Kernel-based methods, combined with ordinary least squares estimation, are used and time series errors are allowed. In addition, these techniques are also implemented for both parametric (linear) and nonparametric regression models.
	"""
	
	cran = "PLRModels" 

	version("1.4", md5="72cecf9053df4054be55888a61cd0559")

