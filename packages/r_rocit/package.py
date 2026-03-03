# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocit(RPackage):
	"""Performance Assessment of Binary Classifier with Visualization

	Sensitivity (or recall or true positive rate), false positive rate, specificity, precision (or positive predictive value), negative predictive value, misclassification rate, accuracy, F-score- these are popular metrics for assessing performance of binary classifier for certain threshold. These metrics are calculated at certain threshold values. Receiver operating characteristic (ROC) curve is a common tool for assessing overall diagnostic ability of the binary classifier. Unlike depending on a certain threshold, area under ROC curve (also known as AUC), is a summary statistic about how well a binary classifier performs overall for the classification task. ROCit package provides flexibility to easily evaluate threshold-bound metrics. Also, ROC curve, along with AUC, can be obtained using different methods, such as empirical, binormal and non-parametric. ROCit encompasses a wide variety of methods for constructing confidence interval of ROC curve and AUC. ROCit also features the option of constructing empirical gains table, which is a handy tool for direct marketing. The package offers options for commonly used visualization, such as, ROC curve, KS plot, lift plot. Along with in-built default graphics setting, there are rooms for manual tweak by providing the necessary values as function arguments. ROCit is a powerful tool offering a range of things, yet it is very easy to use. 
	"""
	
	cran = "ROCit" 

	version("2.1.1", md5="4c3fabfdc2925c5a5c27ebeedecfbb90")

