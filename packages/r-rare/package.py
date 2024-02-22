# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRare(RPackage):
	"""Linear Model with Tree-Based Lasso Regularization for Rare
Features

	Implementation of an alternating direction method of multipliers
    algorithm for fitting a linear model with tree-based lasso regularization, 
    which is proposed in Algorithm 1 of Yan and Bien (2018) <arXiv:1803.06675>. 
    The package allows efficient model fitting on the entire 2-dimensional 
    regularization path for large datasets. The complete set of functions 
    also makes the entire process of tuning regularization parameters and 
    visualizing results hassle-free.
	"""
	
	homepage = "https://github.com/yanxht/rare"
	cran = "rare" 

	version("0.1.1", md5="a95e2eb569a46187d820146d8df0a9f0")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
