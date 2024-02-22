# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQindex(RPackage):
	"""Continuous and Dichotomized Index Predictors Based on
Distribution Quantiles

	Select optimal functional regression or dichotomized quantile
        predictors for survival/logistic/numeric outcome and perform
        optimistic bias correction for any optimally dichotomized numeric
        predictor(s), as in Yi, et. al. (2023)
        <doi:10.1016/j.labinv.2023.100158>.
	"""
	
	cran = "Qindex" 

	version("0.1.5", md5="b05f3f9003777e8b27da0ab22e565274")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
