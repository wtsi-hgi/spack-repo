# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIranges(RPackage):
	"""Foundation of integer range manipulation in Bioconductor.

	Provides efficient low-level and highly reusable S4 classes for storing,
	manipulating and aggregating over annotated ranges of integers.
	Implements an algebra of range operations, including efficient
	algorithms for finding overlaps and nearest neighbors. Defines efficient
	list-like classes for storing, transforming and aggregating large
	grouped data, i.e., collections of atomic vectors and DataFrames."""

	bioc = "IRanges"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IRanges_2.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IRanges/IRanges_2.36.0.tar.gz"]

	version("2.36.0", md5="87618d2e5ee94d7ab81d2e1c4d847120")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.39.2:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
