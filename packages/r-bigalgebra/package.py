# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigalgebra(RPackage):
	"""'BLAS' and 'LAPACK' Routines for Native R Matrices and 'big.matrix'
	Objects.

	Provides arithmetic functions for R matrix and 'big.matrix' objects as well
	as functions for QR factorization, Cholesky factorization, General
	eigenvalue, and Singular value decomposition (SVD). A method matrix
	multiplication and an arithmetic method -for matrix addition, matrix
	difference- allows for mixed type operation -a matrix class object and a
	big.matrix class object- and pure type operation for two big.matrix class
	objects."""

	cran = "bigalgebra"

	version("1.1.1", md5="1d678109e695855a82a6a64949d4e731")

	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
