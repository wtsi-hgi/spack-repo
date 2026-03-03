# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredcrg(RPackage):
	"""Computational Prediction of Proteins Encoded by Circadian Genes

	A computational model for predicting proteins encoded by circadian genes. The support vector machine has been employed with Laplace kernel for prediction of circadian proteins, where compositional, transitional and physico-chemical features were utilized as numeric features. User can predict for the test dataset using the proposed computational model. Besides, the user can also build their own training model using their training dataset, followed by prediction for the test set. 
	"""
	
	cran = "PredCRG" 

	version("1.0.2", md5="39768a5f3b3f490cc3059421af77fe63")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-protr", type=("build", "run"))
	depends_on("r-peptides", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
