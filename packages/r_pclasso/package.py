# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPclasso(RPackage):
	"""Principal Components Lasso

	A method for fitting the entire regularization path 
    of the principal components lasso for linear and
    logistic regression models. The algorithm uses cyclic coordinate descent
    in a path-wise fashion. See URL below for more information on the algorithm.
    See Tay, K., Friedman, J. ,Tibshirani, R., (2014) 'Principal component-guided sparse regression'
    <arXiv:1810.04651>.
	"""
	
	homepage = "https://arxiv.org/abs/1810.04651"
	cran = "pcLasso" 

	version("1.2", md5="fd746e00bc20f4ee08edb677386cec88")

	depends_on("r-svd", type=("build", "run"))
