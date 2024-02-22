# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelayedarray(RPackage):
	"""A unified framework for working transparently with on-disk and in-memory
	array-like datasets.

	Wrapping an array-like object (typically an on-disk object) in a
	DelayedArray object allows one to perform common array operations on it
	without loading the object in memory. In order to reduce memory usage
	and optimize performance, operations on the object are either delayed or
	executed using a block processing mechanism. Note that this also works
	on in-memory array-like objects like DataFrame objects (typically with
	Rle columns), Matrix objects, and ordinary arrays and data frames."""

	bioc = "DelayedArray"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DelayedArray_0.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DelayedArray/DelayedArray_0.28.0.tar.gz"]

	version("0.28.0", md5="812e7575d6eaa61f5b68364cdf1da3d9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics@0.43.4:", type=("build", "run"))
	depends_on("r-matrixgenerics@1.1.3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges@2.17.3:", type=("build", "run"))
	depends_on("r-s4arrays@1.1.1:", type=("build", "run"))
	depends_on("r-sparsearray@1.1.10:", type=("build", "run"))
