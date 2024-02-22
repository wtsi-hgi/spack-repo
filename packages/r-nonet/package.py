# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonet(RPackage):
	"""Weighted Average Ensemble without Training Labels

	It provides ensemble capabilities to supervised and unsupervised learning models predictions without using training labels. It decides the relative weights of the different models predictions by using best models predictions as response variable and rest of the mo. User can decide the best model, therefore, It provides freedom to user to ensemble models based on their design solutions.
	"""
	
	homepage = "https://open.gslab.com/nonet/"
	cran = "nonet" 

	version("0.4.0", md5="f7514e6375d4129c1055a3f6ef4b1406")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret@6.0.78:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlist@0.4.6.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-proc@1.13:", type=("build", "run"))
	depends_on("r-rlang@0.2.1:", type=("build", "run"))
