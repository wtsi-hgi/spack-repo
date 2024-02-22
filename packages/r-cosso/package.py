# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosso(RPackage):
	"""Fit Regularized Nonparametric Regression Models Using COSSO
Penalty

	The COSSO regularization method automatically
        estimates and selects important function components by a
        soft-thresholding penalty in the context of smoothing spline
        ANOVA models. Implemented models include mean regression,
        quantile regression, logistic regression and the Cox regression
        models.
	"""
	
	homepage = "https://arxiv.org/abs/math/0702659"
	cran = "cosso" 

	version("2.1-2", md5="73d0740c1d23064acc5551daded6e9fd")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
