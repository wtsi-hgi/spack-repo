# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelgam(RPackage):
	"""Reluctant Generalized Additive Models

	A method for fitting the entire regularization path of the
    reluctant generalized additive model (RGAM) for linear regression, logistic, 
    Poisson and Cox regression models. See Tay, J. K., and Tibshirani, R., (2019)
    <arXiv:1912.01808> for details.
	"""
	
	homepage = "https://arxiv.org/abs/1912.01808"
	cran = "relgam" 

	version("1.0", md5="6c3f67100d1061b6a6f7434dda2774df")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
