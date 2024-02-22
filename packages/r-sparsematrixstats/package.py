# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsematrixstats(RPackage):
	"""Summary Statistics for Rows and Columns of Sparse Matrices.

	High performance functions for row and column operations on sparse
	matrices.  For example: col / rowMeans2, col / rowMedians, col / rowVars
	etc. Currently, the optimizations are limited to data in the column sparse
	format.  This package is inspired by the matrixStats package by Henrik
	Bengtsson."""

	bioc = "sparseMatrixStats"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/sparseMatrixStats_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/sparseMatrixStats/sparseMatrixStats_1.14.0.tar.gz"]

	version("1.14.0", md5="4319e6fb04b91467bd08cc4ce2ad609c")

	depends_on("r-matrixgenerics@1.5.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats@0.60:", type=("build", "run"))
