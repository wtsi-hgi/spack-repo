# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH2o(RPackage):
	"""R Interface for the 'H2O' Scalable Machine Learning Platform

	R interface for 'H2O', the scalable open source machine learning
    platform that offers parallelized implementations of many supervised and
    unsupervised machine learning algorithms such as Generalized Linear
    Models (GLM), Gradient Boosting Machines (including XGBoost), Random Forests,
    Deep Neural Networks (Deep Learning), Stacked Ensembles, Naive Bayes,
    Generalized Additive Models (GAM), ANOVA GLM, Cox Proportional Hazards, K-Means, PCA, ModelSelection,
    Word2Vec, as well as a fully automatic machine learning algorithm (H2O AutoML).
	"""
	
	homepage = "https://github.com/h2oai/h2o-3"
	cran = "h2o" 

	version("3.44.0.3", md5="e84fa7b9a3bcc54b1831c26abb41b4f2")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
