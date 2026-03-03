# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMikropml(RPackage):
	"""User-Friendly R Package for Supervised Machine Learning
Pipelines

	An interface to build machine learning models for
    classification and regression problems. 'mikropml' implements the ML
    pipeline described by Topçuoğlu et al. (2020)
    <doi:10.1128/mBio.00434-20> with reasonable default options for data
    preprocessing, hyperparameter tuning, cross-validation, testing, model
    evaluation, and interpretation steps.  See the website
    <https://www.schlosslab.org/mikropml/> for more information,
    documentation, and examples.
	"""
	
	homepage = "https://www.schlosslab.org/mikropml/"
	cran = "mikropml" 

	version("1.6.1", md5="c086b2af8ad9c0d659758985db0f7986")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
