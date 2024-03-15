# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixstats(RPackage):
	"""Functions that Apply to Rows and Columns of Matrices (and to Vectors).

	High-performing functions operating on rows and columns of matrices, e.g.
	col / rowMedians(), col / rowRanks(), and col / rowSds(). Functions
	optimized per data type and for subsetted calculations such that both
	memory usage and processing time is minimized. There are also optimized
	vector-based methods, e.g. binMeans(), madDiff() and weightedMedian()."""

	cran = "matrixStats"

	version("1.2.0", md5="2b68a4df8f1d2199ad9feb9b5a73d219")

	depends_on("r@2.12:", type=("build", "run"))
