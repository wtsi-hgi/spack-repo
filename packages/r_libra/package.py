# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibra(RPackage):
	"""Linearized Bregman Algorithms for Generalized Linear Models

	Efficient procedures for fitting the regularization path
    for linear, binomial, multinomial, Ising and Potts models with lasso,
    group lasso or column lasso(only for multinomial) penalty.
    The package uses Linearized Bregman Algorithm to solve the
    regularization path through iterations. Bregman Inverse Scale Space Differential
    Inclusion solver is also provided for linear model with lasso penalty.
	"""
	
	homepage = "https://arxiv.org/abs/1406.7728"
	cran = "Libra" 

	version("1.7", md5="e9c6eab8173c2903f712a41087429954")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
