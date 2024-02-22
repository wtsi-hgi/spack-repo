# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcen(RPackage):
	"""Multivariate Cluster Elastic Net

	Fits the Multivariate Cluster Elastic Net (MCEN) presented in Price & Sherwood (2018) <arXiv:1707.03530>. The MCEN model simultaneously estimates regression coefficients and a clustering of the responses for a multivariate response model. Currently accommodates the Gaussian and binomial likelihood. 
	"""
	
	cran = "mcen" 

	version("1.2.1", md5="95a013b18b78a5054c312be00b8d5b6e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-faraway", type=("build", "run"))
