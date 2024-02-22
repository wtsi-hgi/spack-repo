# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStabilizedregression(RPackage):
	"""Stabilizing Regression and Variable Selection

	Contains an implementation of 'StabilizedRegression', a regression framework for heterogeneous data introduced in Pfister et al. (2021) <arXiv:1911.01850>. The procedure uses averaging to estimate a regression of a set of predictors X on a response variable Y by enforcing stability with respect to a given environment variable. The resulting regression leads to a variable selection procedure which allows to distinguish between stable and unstable predictors. The package further implements a visualization technique which illustrates the trade-off between stability and predictiveness of individual predictors.
	"""
	
	cran = "StabilizedRegression" 

	version("1.1", md5="038235c310683b7dc28ae8a1597eb571")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
