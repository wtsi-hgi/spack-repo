# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppeigen(RPackage):
	"""'Rcpp' Integration for the 'Eigen' Templated Linear Algebra Library.

	R and 'Eigen' integration using 'Rcpp'. 'Eigen' is a C++ template library
	for linear algebra: matrices, vectors, numerical solvers and related
	algorithms. It supports dense and sparse matrices on integer, floating
	point and complex numbers, decompositions of such matrices, and solutions
	of linear systems. Its performance on many algorithms is comparable with
	some of the best implementations based on 'Lapack' and level-3 'BLAS'. The
	'RcppEigen' package includes the header files from the 'Eigen' C++ template
	library (currently version 3.2.8). Thus users do not need to install
	'Eigen' itself in order to use 'RcppEigen'. Since version 3.1.1, 'Eigen' is
	licensed under the Mozilla Public License (version 2); earlier version were
	licensed under the GNU LGPL version 3 or later.  'RcppEigen' (the 'Rcpp'
	bindings/bridge to 'Eigen') is licensed under the GNU GPL version 2 or
	later, as is the rest of 'Rcpp'."""

	cran = "RcppEigen"

	version("0.3.3.9.4", md5="0d107cf6756db5ae44d75e75bd6c7b50")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
