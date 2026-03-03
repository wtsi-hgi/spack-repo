# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorelearn(RPackage):
	"""Classification, Regression and Feature Evaluation

	A suite of machine learning algorithms written in C++ with the R 
 interface contains several learning techniques for classification and regression.
 Predictive models include e.g., classification and regression trees with
 optional constructive induction and models in the leaves, random forests, kNN, 
 naive Bayes, and locally weighted regression. All predictions obtained with these
 models can be explained and visualized with the 'ExplainPrediction' package.  
 This package is especially strong in feature evaluation where it contains several variants of
 Relief algorithm and many impurity based attribute evaluation functions, e.g., Gini, 
 information gain, MDL, and DKM. These methods can be used for feature selection 
 or discretization of numeric attributes.
 The OrdEval algorithm and its visualization is used for evaluation
 of data sets with ordinal features and class, enabling analysis according to the 
 Kano model of customer satisfaction. 
 Several algorithms support parallel multithreaded execution via OpenMP.  
 The top-level documentation is reachable through ?CORElearn.
	"""
	
	homepage = "http://lkm.fri.uni-lj.si/rmarko/software/"
	cran = "CORElearn" 

	version("1.57.3", md5="d4df2df528011ffda46bfea1e5104b67")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
