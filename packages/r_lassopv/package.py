# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLassopv(RPackage):
	"""Nonparametric P-Value Estimation for Predictors in Lasso

	Estimate the p-values for predictors x against target variable y in lasso regression, using the regularization strength when each predictor enters the active set of regularization path for the first time as the statistic. This is based on the assumption that predictors (of the same variance) that (first) become active earlier tend to be more significant. Three null distributions are supported: normal and spherical, which are computed separately for each predictor and analytically under approximation, which aims at efficiency and accuracy for small p-values.
	"""
	
	homepage = "https://github.com/lingfeiwang/lassopv"
	cran = "lassopv" 

	version("0.2.0", md5="d539e6109681125bae8190a60c04abe3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
