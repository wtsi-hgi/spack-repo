# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTornado(RPackage):
	"""Plots for Model Sensitivity and Variable Importance

	Draws tornado plots for model sensitivity to univariate changes.  Implements methods for many modeling methods including linear models, generalized linear models, survival regression models, and arbitrary machine learning models in the caret package.  Also draws variable importance plots.  
	"""
	
	homepage = "https://github.com/bertcarnell/tornado"
	cran = "tornado" 

	version("0.1.3", md5="9301e080ff59c7d57a423ef025ff9f04")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
