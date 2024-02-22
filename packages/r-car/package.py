# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCar(RPackage):
	"""Companion to Applied Regression.

	Functions and Datasets to Accompany J. Fox and S. Weisberg, An R Companion
	to Applied Regression, Second Edition, Sage, 2011."""

	cran = "car"

	version("3.1-2", md5="f8be85a665aa367951aacf80d89eb5e9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cardata@3.0.0:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pbkrtest@0.4.4:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-lme4@1.1.27.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
