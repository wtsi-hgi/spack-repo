# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelimppcr(RPackage):
	"""Relative Importance PCA Regression

	Performs Principal Components Analysis (also known as PCA) dimensionality reduction in the context of a linear regression. In most cases, PCA dimensionality reduction is performed independent of the response variable for a regression. This captures the majority of the variance of the model's predictors, but may not actually be the optimal dimensionality reduction solution for a regression against the response variable. An alternative method, optimized for a regression against the response variable, is to use both PCA and a relative importance measure. This package applies PCA to a given data frame of predictors, and then calculates the relative importance of each PCA factor against the response variable. It outputs ordered factors that are optimized for model fit. By performing dimensionality reduction with this method, an individual can achieve a the same r-squared value as performing just PCA, but with fewer PCA factors. References: Yuri Balasanov (2017) <https://ilykei.com>.
	"""
	
	homepage = "https://github.com/mhernan88/RelimpPCR"
	cran = "RelimpPCR" 

	version("0.3.0", md5="0f72657fa794c31ea1dc707e62168077")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-relaimpo", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
