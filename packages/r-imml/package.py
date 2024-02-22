# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImml(RPackage):
	"""Machine Learning Algorithms Fitting and Validation for Forestry

	Fitting and validation of machine learning algorithms
             for volume prediction of trees, currently for conifer trees based on
			 diameter at breast height and height as explanatory variables.
	"""
	
	cran = "ImML" 

	version("0.1.5", md5="d5abfafa7510bbd56654bb302d9092a2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-rpart@4.1.19:", type=("build", "run"))
	depends_on("r-caret@6.0.94:", type=("build", "run"))
	depends_on("r-randomforest@4.7.1.1:", type=("build", "run"))
	depends_on("r-e1071@1.7.13:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
