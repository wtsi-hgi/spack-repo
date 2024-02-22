# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredhyGui(RPackage):
	"""Genomic Prediction of Hybrid Performance with Graphical User
Interface

	Performs genomic prediction of hybrid performance using eight GS methods including GBLUP, BayesB, RKHS, PLS, LASSO, Elastic net, Random forest and XGBoost.
             GBLUP: genomic best liner unbiased prediction, RKHS: reproducing kernel Hilbert space, PLS: partial least squares regression, LASSO: least absolute shrinkage and selection operator, XGBoost: extreme gradient boosting.
             It also provides fast cross-validation and mating design scheme for training population (Xu S et al (2016) <doi:10.1111/tpj.13242>; Xu S (2017) <doi:10.1534/g3.116.038059>).
	"""
	
	cran = "predhy.GUI" 

	version("1.0", md5="dd7f961198d9ef63889b50004dfccb3f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-predhy@1.2.1:", type=("build", "run"))
	depends_on("r-bglr", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
