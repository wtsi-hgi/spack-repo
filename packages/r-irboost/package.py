# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrboost(RPackage):
	"""Iteratively Reweighted Boosting for Robust Analysis

	Fit a predictive model with the iteratively reweighted boosting (IRBoost) that minimizes the robust loss functions in the CC-family (concave-convex). The convex optimization is conducted by functional descent boosting algorithm in the R package 'xgboost'. The IRBoost reduces the weight of the observation that leads to a large loss; it also provides weights to help identify outliers. Applications include the robust generalized linear models and extensions, where the mean is related to the predictors by boosting, and robust accelerated failure time models. The package supersedes the R package 'ccboost'. Wang (2021) <arXiv:2101.07718>.
	"""
	
	cran = "irboost" 

	version("0.1-1.3", md5="3f9c13136908d8758f92b1b1a7d400e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mpath@0.4.2.21:", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
