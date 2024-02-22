# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredkmeans(RPackage):
	"""Covariate Adaptive Clustering

	Implements the predictive k-means method for clustering observations, using a mixture of experts model to allow covariates to influence cluster centers. Motivated by air pollution epidemiology settings, where cluster membership needs to be predicted across space. Includes functions for predicting cluster membership using spatial splines and principal component analysis (PCA) scores using either multinomial logistic regression or support vector machines (SVMs). For method details see Keller et al. (2017) <doi:10.1214/16-AOAS992>.
	"""
	
	cran = "predkmeans" 

	version("0.1.1", md5="f8e1966da164b8a1678f4693e7fa30a2")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
