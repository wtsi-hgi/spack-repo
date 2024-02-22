# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivarsel(RPackage):
	"""Variable Selection in a Multivariate Linear Model

	It performs variable selection in a multivariate linear model by estimating the covariance matrix 
 of the residuals then use it to remove the dependence that may exist among the responses and eventually performs variable selection by using the Lasso criterion.
 The method is described in the paper Perrot-Dockès et al. (2017) <arXiv:1704.00076>.
	"""
	
	cran = "MultiVarSel" 

	version("1.1.3", md5="a9d47814a8a8fc4215c246c39e9caaa5")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix@1.2.11:", type=("build", "run"))
