# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrassmat(RPackage):
	"""Conditional Random Sampling Sparse Matrices

	Conducts conditional random sampling on observed values in sparse matrices. Useful for training and test set splitting sparse matrices prior to model fitting in cross-validation procedures and estimating the predictive accuracy of data imputation methods, such as matrix factorization or singular value decomposition (SVD). Although designed for applications with sparse matrices, CRASSMAT can also be applied to complete matrices, as well as to those containing missing values.
	"""
	
	cran = "crassmat" 

	version("0.0.6", md5="f9aaf8447bfcc2d74afdcaab3a73f072")

	depends_on("r-svmisc", type=("build", "run"))
