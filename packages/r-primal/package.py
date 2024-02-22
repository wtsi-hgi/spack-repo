# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimal(RPackage):
	"""Parametric Simplex Method for Sparse Learning

	Implements a unified framework of parametric simplex method for a variety of sparse learning problems (e.g., Dantzig selector (for linear regression), sparse quantile regression, sparse support vector machines, and compressive sensing) combined with efficient hyper-parameter selection strategies. The core algorithm is implemented in C++ with Eigen3 support for portable high performance linear algebra. For more details about parametric simplex method, see Haotian Pang (2017) <https://papers.nips.cc/paper/6623-parametric-simplex-method-for-sparse-learning.pdf>.
	"""
	
	cran = "PRIMAL" 

	version("1.0.2", md5="9b2842016e63f3aec34274282d17436f")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
