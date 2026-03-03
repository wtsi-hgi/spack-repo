# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROknne(RPackage):
	"""A k-Nearest Neighbours Ensemble via Optimal Model Selection for
Regression

	Optimal k Nearest Neighbours Ensemble is an ensemble of base k nearest neighbour models each constructed on a bootstrap sample with a random subset of features. k closest observations are identified for a test point "x" (say), in each base k nearest neighbour model to fit a stepwise regression to predict the output value of "x". The final predicted value of "x" is the mean of estimates given by all the models. The implemented model takes training and test datasets and trains the model on training data to predict the test data. Ali, A., Hamraz, M., Kumam, P., Khan, D.M., Khalil, U., Sulaiman, M. and Khan, Z. (2020) <DOI:10.1109/ACCESS.2020.3010099>.
	"""
	
	cran = "OkNNE" 

	version("1.0.1", md5="bc5ba6822cf039e3e59802c45e11a950")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
