# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixgenerics(RPackage):
	"""S4 Generic Summary Statistic Functions that Operate on Matrix-Like
	Objects.

	S4 generic functions modeled after the 'matrixStats' API for alternative
	matrix implementations. Packages with alternative matrix implementation can
	depend on this package and implement the generic functions that are defined
	here for a useful set of row and column summary statistics. Other package
	developers can import this package and handle a different matrix
	implementations without worrying about incompatibilities."""

	bioc = "MatrixGenerics"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MatrixGenerics_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MatrixGenerics/MatrixGenerics_1.14.0.tar.gz"]

	version("1.14.0", md5="18c3a5cc993ca5c2ad48dde1813105e6")

	depends_on("r-matrixstats@1:", type=("build", "run"))
