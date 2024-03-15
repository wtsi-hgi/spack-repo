# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpred(RPackage):
	"""Improved Predictors.

	Improved predictive models by indirect classification and bagging for
	classification, regression and survival problems  as well as resampling
	based estimators of prediction error."""

	cran = "ipred"

	license("GPL-2.0-or-later")

	version("0.9-14", md5="0b1c729529b61d874baf7931f3175b39")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rpart@3.1.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
