# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrnet(RPackage):
	"""Delete or Merge Regressors Algorithms for Linear and Logistic
Model Selection and High-Dimensional Data

	Model selection algorithms for regression and classification, where the predictors can be continuous or categorical and the number of regressors may exceed the number of observations. The selected model consists of a subset of numerical regressors and partitions of levels of factors. Szymon Nowakowski, Piotr Pokarowski, Wojciech Rejchel and Agnieszka Sołtys, 2023. Improving Group Lasso for High-Dimensional Categorical Data. In: Computational Science – ICCS 2023. Lecture Notes in Computer Science, vol 14074, p. 455-470. Springer, Cham. <doi:10.1007/978-3-031-36021-3_47>. Aleksandra Maj-Kańska, Piotr Pokarowski and Agnieszka Prochenka, 2015. Delete or merge regressors for linear model selection. Electronic Journal of Statistics 9(2): 1749-1778. <doi:10.1214/15-EJS1050>. Piotr Pokarowski and Jan Mielniczuk, 2015. Combined l1 and greedy l0 penalized least squares for linear model selection. Journal of Machine Learning Research 16(29): 961-992. <https://www.jmlr.org/papers/volume16/pokarowski15a/pokarowski15a.pdf>. Piotr Pokarowski, Wojciech Rejchel, Agnieszka Sołtys, Michał Frej and Jan Mielniczuk, 2022. Improving Lasso for model selection and prediction. Scandinavian Journal of Statistics, 49(2): 831–863. <doi:10.1111/sjos.12546>.
	"""
	
	homepage = "https://github.com/SzymonNowakowski/DMRnet"
	cran = "DMRnet" 

	version("0.4.0", md5="94f1bd792f0648a5503dbe27dde62256")

	depends_on("r-hclust1d", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
