# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcpc(RPackage):
	"""Flexible Co-Data Learning for High-Dimensional Prediction

	Fit linear, logistic and Cox survival regression models penalised with adaptive multi-group ridge penalties.
  The multi-group penalties correspond to groups of covariates defined by (multiple) co-data sources.
  Group hyperparameters are estimated with an empirical Bayes method of moments, penalised with an extra level of hyper shrinkage.
  Various types of hyper shrinkage may be used for various co-data.
  Co-data may be continuous or categorical. 
  The method accommodates inclusion of unpenalised covariates, posterior selection of covariates and multiple data types.
  The model fit is used to predict for new samples.
  The name 'ecpc' stands for Empirical Bayes, Co-data learnt, Prediction and Covariate selection.
  See Van Nee et al. (2020) <arXiv:2005.04010>.
	"""
	
	homepage = "http://dx.doi.org/10.1002/sim.9162"
	cran = "ecpc" 

	version("3.1.1", md5="d60f0591e1662a857c62fc308f01b7ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gglasso", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-multiridge@1.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-jops", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
