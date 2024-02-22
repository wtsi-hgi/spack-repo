# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL0ara(RPackage):
	"""Sparse Generalized Linear Model with L0 Approximation for
Feature Selection

	An efficient procedure for feature selection for generalized linear models with L0 penalty, including linear, logistic, Poisson, gamma, inverse Gaussian regression. Adaptive ridge algorithms are used to fit the models.
	"""
	
	cran = "l0ara" 

	version("0.1.6", md5="f96b784882f7235872c899afc3f07dc7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
