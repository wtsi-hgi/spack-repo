# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrecsys(RPackage):
	"""Environment for Evaluating Recommender Systems

	Processes standard recommendation datasets (e.g., a user-item rating matrix) as input and generates rating predictions and lists of recommended items. Standard algorithm implementations which are included in this package are the following: Global/Item/User-Average baselines, Weighted Slope One, Item-Based KNN, User-Based KNN, FunkSVD, BPR and weighted ALS. They can be assessed according to the standard offline evaluation methodology (Shani, et al. (2011) <doi:10.1007/978-0-387-85820-3_8>) for recommender systems using measures such as MAE, RMSE, Precision, Recall, F1, AUC, NDCG, RankScore and coverage measures. The package (Coba, et al.(2017) <doi: 10.1007/978-3-319-60042-0_36>) is intended for rapid prototyping of recommendation algorithms and education purposes. 
	"""
	
	homepage = "https://rrecsys.inf.unibz.it/"
	cran = "rrecsys" 

	version("0.9.7.3.1", md5="1d02add1ca685cfe0f8eb5dcb68c271b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-registry", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
