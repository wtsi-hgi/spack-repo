# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REngression(RPackage):
	"""Engression Modelling

	Fits engression models for nonlinear distributional regression. Predictors and targets can be univariate or multivariate. Functionality includes estimation of conditional mean, estimation of conditional quantiles, or sampling from the fitted distribution. Training is done full-batch on CPU (the python version offers GPU-accelerated stochastic gradient descent). Based on "Engression: Extrapolation for nonlinear regression?" by Xinwei Shen and Nicolai Meinshausen (2023). Also supports classification (experimental). 
 <arxiv:2307.00835>.
	"""
	
	homepage = "https://github.com/xwshen51/engression/"
	cran = "engression" 

	version("0.1.4", md5="97a4491295f41dd47020b0d6429fc212")

	depends_on("r-torch", type=("build", "run"))
