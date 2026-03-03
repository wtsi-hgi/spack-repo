# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpath(RPackage):
	"""Regularized Linear Models

	Algorithms compute robust estimators for loss functions in the concave convex (CC) family by the iteratively reweighted convex optimization (IRCO), an extension of the iteratively reweighted least squares (IRLS). The IRCO reduces the weight of the observation that leads to a large loss; it also provides weights to help identify outliers. Applications include robust (penalized) generalized linear models and robust support vector machines. The package also contains penalized Poisson, negative binomial, zero-inflated Poisson, zero-inflated negative binomial regression models and robust models with non-convex loss functions. Wang et al. (2014) <doi:10.1002/sim.6314>,
      Wang et al. (2015) <doi:10.1002/bimj.201400143>,
      Wang et al. (2016) <doi:10.1177/0962280214530608>,
      Wang (2021) <doi:10.1007/s11749-021-00770-2>,
      Wang (2024) <doi:10.1111/anzs.12409>.
	"""
	
	homepage = "https://github.com/zhuwang46/mpath"
	cran = "mpath" 

	version("0.4-2.25", md5="c61fd27a157d0b2923cd48d738a02372")
	version("0.4-2.23", md5="cbd4020eba60f8fbd0fa67aff2c0aabc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-bst", type=("build", "run"))
	depends_on("r-weightsvm", type=("build", "run"))
