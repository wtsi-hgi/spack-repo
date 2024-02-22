# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasen(RPackage):
	"""Random Subspace Ensemble Classification and Variable Screening

	We propose a general ensemble classification framework, RaSE algorithm, for the sparse classification problem. In RaSE algorithm, for each weak learner, some random subspaces are generated and the optimal one is chosen to train the model on the basis of some criterion. To be adapted to the problem, a novel criterion, ratio information criterion (RIC) is put up with based on Kullback-Leibler divergence. Besides minimizing RIC, multiple criteria can be applied, for instance, minimizing extended Bayesian information criterion (eBIC), minimizing training error, minimizing the validation error, minimizing the cross-validation error, minimizing leave-one-out error. There are various choices of base classifier, for instance, linear discriminant analysis, quadratic discriminant analysis, k-nearest neighbour, logistic regression, decision trees, random forest, support vector machines. RaSE algorithm can also be applied to do feature ranking, providing us the importance of each feature based on the selected percentage in multiple subspaces. RaSE framework can be extended to the general prediction framework, including both classification and regression. We can use the selected percentages of variables for variable screening. The latest version added the variable screening function for both regression and classification problems. 
	"""
	
	cran = "RaSEn" 

	version("3.0.0", md5="85235ce3058338982965be3f68db15b6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-kernelknn", type=("build", "run"))
	depends_on("r-modelmetrics", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
