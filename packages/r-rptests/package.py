# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRptests(RPackage):
	"""Goodness of Fit Tests for High-Dimensional Linear Regression
Models

	Performs goodness of fits tests for both high and low-dimensional linear models.
    It can test for a variety of model misspecifications including nonlinearity and heteroscedasticity.
    In addition one can test the significance of potentially large groups of variables, and also
    produce p-values for the significance of individual variables in high-dimensional linear
    regression.
	"""
	
	homepage = "https://rss.onlinelibrary.wiley.com/doi/10.1111/rssb.12234"
	cran = "RPtests" 

	version("0.1.5", md5="040fc926f9040d9ca8ea34ee2bbd2294")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
