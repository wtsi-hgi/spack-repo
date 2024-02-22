# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepregression(RPackage):
	"""Fitting Deep Distributional Regression

	
    Allows for the specification of semi-structured deep distributional regression models which are fitted in a neural network as 
    proposed by Ruegamer et al. (2023) <doi:10.18637/jss.v105.i02>.
    Predictors can be modeled using structured (penalized) linear effects, structured non-linear effects or using an unstructured deep network model.
	"""
	
	cran = "deepregression" 

	version("1.0.0", md5="97ff9ea94516640bd20066523a76f543")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tensorflow@2.2:", type=("build", "run"))
	depends_on("r-tfprobability", type=("build", "run"))
	depends_on("r-keras@2.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reticulate@1.14:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tfruns", type=("build", "run"))
