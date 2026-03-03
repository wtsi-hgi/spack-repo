# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedcl(RPackage):
	"""Efficient and Feasible Inference for High-Dimensional Normal
Copula Regression Models

	Estimates high-dimensional multivariate normal copula regression models with the weighted composite likelihood estimating equations in Nikoloulopoulos (2022) <arXiv:2203.04619>. It provides autoregressive moving average correlation structures and binary, ordinal, Poisson, and negative binomial regressions.
	"""
	
	cran = "weightedCL" 

	version("0.5", md5="42c26852e02d87d9ad011bb2fe726b50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-sure", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
