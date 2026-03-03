# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdme(RPackage):
	"""High-Dimensional Regression with Measurement Error

	Penalized regression for generalized linear models for
  measurement error problems (aka. errors-in-variables). The package
  contains a version of the lasso (L1-penalization) which corrects
  for measurement error (Sorensen et al. (2015) <doi:10.5705/ss.2013.180>). 
  It also contains an implementation of the Generalized Matrix Uncertainty 
  Selector, which is a version the (Generalized) Dantzig Selector for the 
  case of measurement error (Sorensen et al. (2018) <doi:10.1080/10618600.2018.1425626>).
	"""
	
	homepage = "https://github.com/osorensen/hdme"
	cran = "hdme" 

	version("0.6.0", md5="f0bb858ebceaa0621d7b8b149c6672d8")

	depends_on("r-glmnet@3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rglpk@0.6.1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
