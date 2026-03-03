# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoil(RPackage):
	"""Sparsity Oriented Importance Learning

	Sparsity Oriented Importance Learning (SOIL) provides a new variable importance measure for high dimensional linear regression and logistic regression from a sparse penalization perspective, by taking into account the variable selection uncertainty via the use of a sensible model weighting. The package is an implementation of Ye, C., Yang, Y., and Yang, Y. (2017+).
	"""
	
	homepage = "https://github.com/emeryyi/SOIL"
	cran = "SOIL" 

	version("1.1", md5="836cdf5ab439a3751be1771a84ff8743")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-brglm2", type=("build", "run"))
