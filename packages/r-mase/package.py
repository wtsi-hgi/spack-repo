# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMase(RPackage):
	"""Model-Assisted Survey Estimators

	A set of model-assisted survey estimators and corresponding
    variance estimators for single stage, unequal probability, without replacement
    sampling designs.  All of the estimators can be written as a generalized 
    regression estimator with the Horvitz-Thompson, ratio, post-stratified, and 
    regression estimators summarized by Sarndal et al. (1992, ISBN:978-0-387-40620-6).
    Two of the estimators employ a statistical learning model as the assisting model:
    the elastic net regression estimator, which is an extension of the lasso regression
    estimator given by McConville et al. (2017) <doi:10.1093/jssam/smw041>, and the 
    regression tree estimator described in McConville and Toth (2017) <arXiv:1712.05708>. 
    The variance estimators which approximate the joint inclusion probabilities can
    be found in Berger and Tille (2009) <doi:10.1016/S0169-7161(08)00002-3> and the
    bootstrap variance estimator is presented in Mashreghi et al. (2016) 
    <doi:10.1214/16-SS113>.
	"""
	
	cran = "mase" 

	version("0.1.5.2", md5="e4f3e98a7da3fd4537eaffd321640dae")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rpms", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
