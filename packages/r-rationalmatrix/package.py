# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRationalmatrix(RPackage):
	"""Exact Matrix Algebra for Rational Matrices

	Provides functions to deal with matrix algebra for matrices
    with rational entries: determinant, rank, image and kernel, inverse,
    Cholesky decomposition. All computations are exact.
	"""
	
	homepage = "https://github.com/stla/RationalMatrix"
	cran = "RationalMatrix" 

	version("1.0.0", md5="06322c4a28f002a22026cdffad09fbfd")

	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
