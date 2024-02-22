# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanic(RPackage):
	"""Solving Ax = b Nimbly in C++

	Routines for solving large systems of linear equations and
  eigenproblems in R. Direct and iterative solvers from the Eigen C++ library
  are made available. Solvers include Cholesky, LU, QR, and Krylov subspace
  methods (Conjugate Gradient, BiCGSTAB). Dense and sparse problems are
  supported.
	"""
	
	homepage = "https://github.com/nk027/sanic"
	cran = "sanic" 

	version("0.0.2", md5="ec1ba1ff425cb251f5c375268e28a085")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
