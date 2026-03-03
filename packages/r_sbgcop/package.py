# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbgcop(RPackage):
	"""Semiparametric Bayesian Gaussian Copula Estimation and
Imputation

	Estimation and inference for parameters in a Gaussian copula model,
        treating the univariate marginal distributions as nuisance
        parameters as described in Hoff (2007) <doi:10.1214/07-AOAS107>. 
        This package also provides a
        semiparametric imputation procedure for missing multivariate
        data.
	"""
	
	homepage = "http://pdhoff.github.io/"
	cran = "sbgcop" 

	version("0.980", md5="1bbc7851bf08d8e25737cbcbed0801f9")

