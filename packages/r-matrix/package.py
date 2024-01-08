# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrix(RPackage):
	"""Sparse and Dense Matrix Classes and Methods.

	A rich hierarchy of matrix classes, including triangular, symmetric, and
	diagonal matrices, both dense and sparse and with pattern, logical and
	numeric entries.   Numerous methods for and operations on these matrices,
	using 'LAPACK' and 'SuiteSparse' libraries."""

	cran = "Matrix"

	version("1.6-1.1", md5="ef1eb06ffc3ad6c8c955d1b14dd3364f")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
