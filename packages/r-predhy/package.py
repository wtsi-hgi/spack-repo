# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredhy(RPackage):
	"""Genomic Prediction of Hybrid Performance

	Performs genomic prediction of hybrid performance using eight GS methods including GBLUP, BayesB, RKHS, PLS, LASSO, Elastic net, LightGBM and XGBoost. It also provides fast cross-validation and mating design scheme for training population (Xu S et al (2016) <doi:10.1111/tpj.13242>; Xu S (2017) <doi:10.1534/g3.116.038059>). 
	"""
	
	cran = "predhy" 

	version("2.0.1", md5="ac3064f6269efdfc3518b85b3e237630")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-bglr", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-lightgbm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
