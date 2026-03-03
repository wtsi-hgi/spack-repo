# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustmatrix(RPackage):
	"""Robust Matrix-Variate Parameter Estimation

	Robust covariance estimation for matrix-valued data and data with Kronecker-covariance structure using the Matrix Minimum Covariance Determinant (MMCD) estimators and outlier explanation using and Shapley values. 
	"""
	
	cran = "robustmatrix" 

	version("0.1.2", md5="6d7a4ccfe32f46032e348bd423ef1b24")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
