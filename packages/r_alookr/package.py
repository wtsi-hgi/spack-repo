# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlookr(RPackage):
	"""Model Classifier for Binary Classification

	A collection of tools that support data splitting, predictive modeling, and model evaluation. 
    A typical function is to split a dataset into a training dataset and a test dataset. 
    Then compare the data distribution of the two datasets.
    Another feature is to support the development of predictive models and to compare the performance of several predictive models, 
    helping to select the best model. 
	"""
	
	cran = "alookr" 

	version("0.3.9", md5="f29c6375f3cf934a90c79b725a39a0b3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-cli@1.1:", type=("build", "run"))
	depends_on("r-dlookr", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggmosaic", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
