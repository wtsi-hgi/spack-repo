# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalice(RPackage):
	"""Local Individual Conditional Expectation

	Local Individual Conditional Expectation ('localICE') is a local explanation approach from the field of eXplainable Artificial Intelligence (XAI). localICE is a model-agnostic XAI approach which provides three-dimensional local explanations for particular data instances. The approach is proposed in the master thesis of Martin Walter as an extension to ICE (see Reference). The three dimensions are the two features at the horizontal and vertical axes as well as the target represented by different colors. The approach is applicable for classification and regression problems to explain interactions of two features towards the target. For classification models, the number of classes can be more than two and each class is added as a different color to the plot. The given instance is added to the plot as two dotted lines according to the feature values. The localICE-package can explain features of type factor and numeric of any machine learning model. Automatically supported machine learning packages are 'mlr', 'randomForest', 'caret' or all other with an S3 predict function. For further model types from other libraries, a predict function has to be provided as an argument in order to get access to the model. Reference to the ICE approach: Alex Goldstein, Adam Kapelner, Justin Bleich, Emil Pitkin (2013) <arXiv:1309.6392>. 
	"""
	
	homepage = "https://github.com/viadee/localICE"
	cran = "localICE" 

	version("0.1.1", md5="230fd0c5818775e54d8b0630cdeeaea9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
