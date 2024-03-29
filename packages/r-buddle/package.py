# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBuddle(RPackage):
	"""A Deep Learning for Statistical Classification and Regression
Analysis with Random Effects

	Statistical classification and regression have been popular among various fields and stayed in the limelight of scientists of those fields. Examples of the fields include clinical trials where the statistical classification of patients is indispensable to predict the clinical courses of diseases. Considering the negative impact of diseases on performing daily tasks, correctly classifying patients based on the clinical information is vital in that we need to identify patients of the high-risk group to develop a severe state and arrange medical treatment for them at an opportune moment. Deep learning - a part of artificial intelligence - has gained much attention, and research on it burgeons during past decades: see, e.g, Kazemi and Mirroshandel (2018) <DOI:10.1016/j.artmed.2017.12.001>. It is a veritable technique which was originally designed for the classification, and hence, the Buddle package can provide sublime solutions to various challenging classification and regression problems encountered in the clinical trials. The Buddle package is based on the back-propagation algorithm - together with various powerful techniques such as batch normalization and dropout - which performs a multi-layer feed-forward neural network: see Krizhevsky et. al (2017) <DOI:10.1145/3065386>, Schmidhuber (2015) <DOI:10.1016/j.neunet.2014.09.003> and LeCun et al. (1998) <DOI:10.1109/5.726791> for more details. This package contains two main functions: TrainBuddle() and FetchBuddle(). TrainBuddle() builds a feed-forward neural network model and trains the model. FetchBuddle() recalls the trained model which is the output of TrainBuddle(), classifies or regresses given data, and make a final prediction for the data.
	"""
	
	cran = "Buddle" 

	version("2.0.1", md5="6d0b777e5807ab26c486841fbf32f651")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
