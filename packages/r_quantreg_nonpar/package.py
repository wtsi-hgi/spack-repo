# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantregNonpar(RPackage):
	"""Nonparametric Series Quantile Regression

	Implements the nonparametric quantile regression method developed by Belloni, Chernozhukov, and Fernandez-Val (2011) to partially linear quantile models. Provides point estimates of the conditional quantile function and its derivatives based on series approximations to the nonparametric part of the model. Provides pointwise and uniform confidence intervals using analytic and resampling methods.
	"""
	
	cran = "quantreg.nonpar" 

	version("1.0", md5="615375d3137bc12b9d7c0e63999c4288")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-rearrangement", type=("build", "run"))
