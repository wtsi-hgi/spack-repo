# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcboost(RPackage):
	"""Multi-Calibration Boosting

	Implements 'Multi-Calibration Boosting' (2018) <https://proceedings.mlr.press/v80/hebert-johnson18a.html> and
    'Multi-Accuracy Boosting' (2019) <arXiv:1805.12317> for the multi-calibration of a machine learning model's prediction.
    'MCBoost' updates predictions for sub-groups in an iterative fashion in order to mitigate biases like poor calibration or large accuracy differences across subgroups.
    Multi-Calibration works best in scenarios where the underlying data & labels are unbiased, but resulting models are.
    This is often the case, e.g. when an algorithm fits a majority population while ignoring or under-fitting minority populations.
	"""
	
	homepage = "https://github.com/mlr-org/mcboost"
	cran = "mcboost" 

	version("0.4.2", md5="220820c6b15b320e28da93cf5d91b59a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.13.6:", type=("build", "run"))
	depends_on("r-mlr3@0.10:", type=("build", "run"))
	depends_on("r-mlr3misc@0.8:", type=("build", "run"))
	depends_on("r-mlr3pipelines@0.3:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
