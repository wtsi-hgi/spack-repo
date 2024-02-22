# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmlalg(RPackage):
	"""Double Machine Learning Algorithms

	Implementation of double machine learning (DML) algorithms in R, 
    based on Emmenegger and Buehlmann (2021) "Regularizing Double Machine Learning 
    in Partially Linear Endogenous Models" <arXiv:2101.12525> and Emmenegger and
    Buehlmann (2021) <arXiv:2108.13657> "Double Machine Learning for Partially 
    Linear Mixed-Effects Models with Repeated Measurements". 
    First part: our goal is to perform inference for the linear parameter in partially
    linear models with confounding variables.
    The standard DML estimator of the linear parameter has a two-stage least
    squares interpretation, which can lead to a large variance and overwide
    confidence intervals.
    We apply regularization to reduce the variance of the estimator,
    which produces narrower confidence intervals that are approximately valid.
    Nuisance terms can be flexibly estimated with machine learning algorithms.
    Second part: our goal is to estimate and perform inference for the linear 
    coefficient in a partially linear mixed-effects model
    with DML. Machine learning algorithms allows us to incorporate more
    complex interaction structures and high-dimensional variables. 
	"""
	
	homepage = "https://gitlab.math.ethz.ch/ecorinne/dmlalg.git"
	cran = "dmlalg" 

	version("1.0.2", md5="e771ba2d365159a8cdba4bd62ca50f5f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
