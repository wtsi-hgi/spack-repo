# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsechol(RPackage):
	"""Sparse Matrix C++ Classes Including Sparse Cholesky LDL
Decomposition of Symmetric Matrices

	'C++' classes for sparse matrix methods including implementation of sparse LDL decomposition of symmetric matrices and solvers described by Timothy A. Davis (2016) 
  <https://fossies.org/linux/SuiteSparse/LDL/Doc/ldl_userguide.pdf>. Provides a set of C++ classes for basic sparse
  matrix specification and linear algebra, and a class to implement sparse LDL decomposition and solvers. See <https://github.com/samuel-watson/SparseChol>
  for details.
	"""
	
	homepage = "https://github.com/samuel-watson/SparseChol"
	cran = "SparseChol" 

	version("0.3.1", md5="06d848f6e2cd224278cd7c4a340a93c8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix@1.3.4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
