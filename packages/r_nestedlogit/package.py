# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestedlogit(RPackage):
	"""Nested Dichotomy Logistic Regression Models

	Provides functions for specifying and fitting nested
    dichotomy logistic regression models for a multi-category response and
    methods for summarising and plotting those models.  Nested dichotomies are
    statistically independent, and hence provide an additive decomposition
    of tests for the overall 'polytomous' response.  When the dichotomies
    make sense substantively, this method can be a simpler alternative to
    the standard 'multinomial' logistic model which compares response
    categories to a reference level.  See: J. Fox (2016), "Applied
    Regression Analysis and Generalized Linear Models", 3rd Ed., ISBN
    1452205663.
	"""
	
	homepage = "https://github.com/friendly/nestedLogit"
	cran = "nestedLogit" 

	version("0.3.2", md5="c65a531566c40dd6002be97ff1c2a9f3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-effects", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
