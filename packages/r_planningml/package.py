# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanningml(RPackage):
	"""A Sample Size Calculator for Machine Learning Applications in
Healthcare

	Advances in automated document classification has led to identifying massive numbers of clinical concepts from handwritten clinical notes. These high dimensional clinical concepts can serve as highly informative predictors in building classification algorithms for identifying patients with different clinical conditions, commonly referred to as patient phenotyping. However, from a planning perspective, it is critical to ensure that enough data is available for the phenotyping algorithm to obtain a desired classification performance. This challenge in sample size planning is further exacerbated by the high dimension of the feature space and the inherent imbalance of the response class. Currently available sample size planning methods can be categorized into: (i) model-based approaches that predict the sample size required for achieving a desired accuracy using a linear machine learning classifier and (ii) learning curve-based approaches (Figueroa et al. (2012) <doi:10.1186/1472-6947-12-8>) that fit an inverse power law curve to pilot data to extrapolate performance. We develop model-based approaches for imbalanced data with correlated features, deriving sample size formulas for performance metrics that are sensitive to class imbalance such as Area Under the receiver operating characteristic Curve (AUC) and Matthews Correlation Coefficient (MCC). This is done using a two-step approach where we first perform feature selection using the innovated High Criticism thresholding method (Hall and Jin (2010) <doi:10.1214/09-AOS764>), then determine the sample size by optimizing the two performance metrics. Further, we develop software in the form of an R package named 'planningML' and an 'R' 'Shiny' app to facilitate the convenient implementation of the developed model-based approaches and learning curve approaches for imbalanced data. We apply our methods to the problem of phenotyping rare outcomes using the MIMIC-III electronic health record database. We show that our developed methods which relate training data size and performance on AUC and MCC, can predict the true or observed performance from linear ML classifiers such as LASSO and SVM at different training data sizes. Therefore, in high-dimensional classification analysis with imbalanced data and correlated features, our approach can efficiently and accurately determine the sample size needed for machine-learning based classification.
	"""
	
	cran = "planningML" 

	version("1.0.1", md5="be641a181fb93fffc9ba2612fc89420b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
