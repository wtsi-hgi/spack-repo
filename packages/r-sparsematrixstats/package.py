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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sparseMatrixStats_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sparseMatrixStats/sparseMatrixStats_1.14.0.tar.gz"]
    version("1.20.0", tag="RELEASE_3_21")
	version("1.8.0", commit="4f1e2213e5b0d6b3d817c2c9129b7566288916f6")
	version("1.6.0", commit="78627a842790af42b6634893087b2bb1f4ac0392")
	version("1.2.1", commit="9726f3d5e0f03b50c332d85d5e4c339c18b0494c")
	version("1.14.0", sha256="39b1f8dd13df7222e5de6bd1fa0ea1bb931577d10551757c445776a120ef5264")
	version("1.12.0", commit="054bf939cd7220deaf8e768ff7029d0d38483c91")
	version("1.10.0", commit="75d85ba2c9c4c36887fef1a007883167aa85bd94")

	depends_on("r-matrixgenerics@1.5.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats@0.60:", type=("build", "run"))
