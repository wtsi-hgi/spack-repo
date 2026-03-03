# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscretecdalgorithm(RPackage):
	"""Coordinate-Descent Algorithm for Learning Sparse Discrete
Bayesian Networks

	Structure learning of Bayesian network using coordinate-descent
    algorithm. This algorithm is designed for discrete network assuming a multinomial data set,
    and we use a multi-logit model to do the regression.
    The algorithm is described in Gu, Fu and Zhou (2016) <arXiv:1403.2310>.
	"""
	
	cran = "discretecdAlgorithm" 

	version("0.0.7", md5="c4f4501fc700dce591f5674a17a76010")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sparsebnutils@0.0.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
