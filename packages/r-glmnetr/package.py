# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmnetr(RPackage):
	"""Nested Cross Validation for the Relaxed Lasso and Other Machine
Learning Models

	
    Cross validation informed Relaxed LASSO, Artificial Neural Network (ANN), gradient boosting machine ('xgboost'), Random Forest ('RandomForestSRC'), Recursive Partitioning ('RPART') or step wise regression models are fit.  Nested cross validation (or analogous for the random forest) to estimate and compare performances between these models is used to describe model performances.  
    For some datasets, for example when the design matrix is not of full rank, 'glmnet' may have very long run times when fitting the relaxed lasso model, from our experience when fitting Cox models on data with many predictors and many patients, making it difficult to get solutions from either glmnet() or cv.glmnet().  This may be remedied with the 'path=TRUE' options when calling glmnet() and cv.glmnet().  Within the glmnetr package the approach of path=TRUE is taken by default.   
    When fitting not a relaxed lasso model but an elastic-net model, then the R-packages 'nestedcv' <https://cran.r-project.org/package=nestedcv>, 'glmnetSE' <https://cran.r-project.org/package=glmnetSE> or others may provide greater functionality when performing a nested CV.
    As with the 'glmnet' package, this package passes most relevant output to the output object and tabular and graphical summaries can be generated using the summary and plot functions.  Use of the 'glmnetr' has many similarities to the 'glmnet' package and it is recommended that the user of 'glmnetr' first become familiar with the 'glmnet' package <https://cran.r-project.org/package=glmnet>, with the "An Introduction to 'glmnet'" and "The Relaxed Lasso" being especially helpful in this regard.
	"""
	
	cran = "glmnetr" 

	version("0.4-2", md5="a9ec330242ea53d728273d62dbfebcbc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-smoof", type=("build", "run"))
	depends_on("r-mlrmbo", type=("build", "run"))
	depends_on("r-paramhelpers", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
