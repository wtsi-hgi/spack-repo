# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlcv(RPackage):
	"""Nested Loop Cross Validation

	Nested loop cross validation for classification purposes for misclassification error rate estimation.
  The package supports several methodologies for feature selection: random forest, Student t-test, limma, 
  and provides an interface to the following classification methods in the 'MLInterfaces' package: linear, 
  quadratic discriminant analyses, random forest, bagging, prediction analysis for microarray, generalized 
  linear model, support vector machine (svm and ksvm). Visualizations to assess the quality of
  the classifier are included: plot of the ranks of the features, scores plot for a specific 
  classification algorithm and number of features, misclassification rate 
  for the different number of features and classification algorithms tested and ROC plot.
  For further details about the methodology, please check:
  Markus Ruschhaupt, Wolfgang Huber, Annemarie Poustka, and Ulrich Mansmann (2004) 
  <doi:10.2202/1544-6115.1078>.
	"""
	
	cran = "nlcv" 

	version("0.3.5", md5="593ea18b0daa3c430ba4034123511a63")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-a4core", type=("build", "run"))
	depends_on("r-mlinterfaces@1.22:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
