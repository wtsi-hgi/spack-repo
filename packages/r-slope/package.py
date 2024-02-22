# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlope(RPackage):
	"""Sorted L1 Penalized Estimation

	Efficient implementations for Sorted L-One Penalized Estimation
    (SLOPE): generalized linear models regularized with the sorted L1-norm
    (Bogdan et al. (2015) <doi:10/gfgwzt>). Supported models include ordinary
    least-squares regression, binomial regression, multinomial regression, and
    Poisson regression. Both dense and sparse  predictor matrices are supported.
    In addition, the package features predictor screening rules that enable fast
    and efficient solutions to high-dimensional problems.
	"""
	
	homepage = "https://jolars.github.io/SLOPE/"
	cran = "SLOPE" 

	version("0.5.0", md5="55eee60693d9a390d9988cdec8a10cf7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.850.1:", type=("build", "run"))
