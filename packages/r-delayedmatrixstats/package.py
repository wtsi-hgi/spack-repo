# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelayedmatrixstats(RPackage):
	"""Functions that Apply to Rows and Columns of 'DelayedMatrix' Objects.

	A port of the 'matrixStats' API for use with DelayedMatrix objects from
	the 'DelayedArray' package. High-performing functions operating on rows
	and columns of DelayedMatrix objects, e.g. col / rowMedians(), col /
	rowRanks(), and col / rowSds(). Functions optimized per data type and
	for subsetted calculations such that both memory usage and processing
	time is minimized."""

	bioc = "DelayedMatrixStats"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DelayedMatrixStats_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DelayedMatrixStats/DelayedMatrixStats_1.24.0.tar.gz"]

	version("1.24.0", md5="890845d8c80a2b64cd02b3ff7f1e504d")

	depends_on("r-matrixgenerics@1.13.1:", type=("build", "run"))
	depends_on("r-delayedarray@0.27.10:", type=("build", "run"))
	depends_on("r-sparsematrixstats@1.13.2:", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.5:", type=("build", "run"))
	depends_on("r-iranges@2.25.10:", type=("build", "run"))
