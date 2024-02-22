# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErboost(RPackage):
	"""Nonparametric Multiple Expectile Regression via ER-Boost

	Expectile regression is a nice tool for estimating the conditional expectiles of a response variable given a set of covariates. This package implements a regression tree based gradient boosting estimator for nonparametric multiple expectile regression, proposed by Yang, Y., Qian, W. and Zou, H. (2018) <doi:10.1080/00949655.2013.876024>. The code is based on the 'gbm' package originally developed by Greg Ridgeway.
	"""
	
	cran = "erboost" 

	version("1.4", md5="c4a513ef861f91879bcb10fde8590bdb")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
