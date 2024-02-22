# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarrot(RPackage):
	"""Predicting Categorical and Continuous Outcomes Using One in Ten
Rule

	Predicts categorical or continuous outcomes while concentrating on a number of key points. These are Cross-validation, Accuracy, Regression and Rule of Ten or "one in ten rule" (CARRoT), and, in addition to it R-squared statistics, prior knowledge on the dataset etc. It performs the cross-validation specified number of times by partitioning the input into training and test set and fitting linear/multinomial/binary regression models to the training set. All regression models satisfying chosen constraints are fitted and the ones with the best predictive power are given as an output. Best predictive power is understood as highest accuracy in case of binary/multinomial outcomes, smallest absolute and relative errors in case of continuous outcomes. For binary case there is also an option of finding a regression model which gives the highest AUROC (Area Under Receiver Operating Curve) value. The option of parallel toolbox is also available. Methods are described in Peduzzi et al. (1996) <doi:10.1016/S0895-4356(96)00236-3> , Rhemtulla et al. (2012) <doi:10.1037/a0029315>, Riley et al. (2018) <doi:10.1002/sim.7993>, Riley et al. (2019) <doi:10.1002/sim.7992>.
	"""
	
	cran = "CARRoT" 

	version("3.0.2", md5="d3251a5058bfffb8fb1ca88a68391c13")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
