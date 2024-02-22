# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRms(RPackage):
	"""Regression Modeling Strategies.

	Regression modeling, testing, estimation, validation, graphics, prediction,
	and typesetting by storing enhanced model design attributes in the fit.
	'rms' is a collection of functions that assist with and streamline
	modeling. It also contains functions for binary and ordinal logistic
	regression models, ordinal models for continuous Y with a variety of
	distribution families, and the Buckley-James multiple regression model for
	right-censored responses, and implements penalized maximum likelihood
	estimation for logistic and ordinary linear models. 'rms' works with almost
	any regression model, but it was especially written to work with binary or
	ordinal regression models, Cox regression, accelerated failure time models,
	ordinary linear models, the Buckley-James model, generalized least squares
	for serially or spatially correlated observations, generalized linear
	models, and quantile regression."""

	cran = "rms"

	version("6.7-1", md5="93a6eb3c6991b9c579a914d8b59a9a41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hmisc@5.1.0:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-nlme@3.1.123:", type=("build", "run"))
	depends_on("r-polspline", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-htmltable@1.11:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
