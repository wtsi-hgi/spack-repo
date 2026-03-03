# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVbsparsepca(RPackage):
	"""The Variational Bayesian Method for Sparse PCA

	Contains functions for a variational Bayesian method for sparse PCA proposed by Ning (2020) <arXiv:2102.00305>. There are two algorithms: the PX-CAVI algorithm (if assuming the loadings matrix is jointly row-sparse) and the batch PX-CAVI algorithm (if without this assumption). The outputs of the main function, VBsparsePCA(), include the mean and covariance of the loadings matrix, the score functions, the variable selection results, and the estimated variance of the random noise. 
	"""
	
	cran = "VBsparsePCA" 

	version("0.1.0", md5="e3a048118f1c41fbd3491becc5d61409")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
