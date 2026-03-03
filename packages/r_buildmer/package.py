# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBuildmer(RPackage):
	"""Stepwise Elimination and Term Reordering for Mixed-Effects
Regression

	Finds the largest possible regression model that will still converge
    for various types of regression analyses (including mixed models and generalized
    additive models) and then optionally performs stepwise elimination similar to the
    forward and backward effect-selection methods in SAS, based on the change in
    log-likelihood or its significance, Akaike's Information Criterion, the Bayesian
    Information Criterion, the explained deviance, or the F-test of the change in R².
	"""
	
	cran = "buildmer" 

	version("2.11", md5="4c9471fc5d232247509dc06479f5be10")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
