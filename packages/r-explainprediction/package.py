# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExplainprediction(RPackage):
	"""Explanation of Predictions for Classification and Regression
Models

	Generates explanations for classification and regression models and visualizes them.
 Explanations are generated for individual predictions as well as for models as a whole. Two explanation methods
 are included, EXPLAIN and IME. The EXPLAIN method is fast but might miss explanations expressed redundantly
 in the model. The IME method is slower as it samples from all feature subsets.
 For the EXPLAIN method see Robnik-Sikonja and Kononenko (2008) <doi:10.1109/TKDE.2007.190734>, 
 and the IME method is described in Strumbelj and Kononenko (2010, JMLR, vol. 11:1-18).
 All models in package 'CORElearn' are natively supported, for other prediction models a wrapper function is provided 
 and illustrated for models from packages 'randomForest', 'nnet', and 'e1071'.
	"""
	
	homepage = "http://lkm.fri.uni-lj.si/rmarko/software/"
	cran = "ExplainPrediction" 

	version("1.3.0", md5="0ef3002e1bbfcb0d601146faa8162485")

	depends_on("r-corelearn@1.52:", type=("build", "run"))
	depends_on("r-semiartificial@2.2.5:", type=("build", "run"))
