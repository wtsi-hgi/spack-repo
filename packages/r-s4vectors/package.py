# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS4vectors(RPackage):
	"""Foundation of vector-like and list-like containers in Bioconductor.

	The S4Vectors package defines the Vector and List virtual classes and a
	set of generic functions that extend the semantic of ordinary vectors
	and lists in R. Package developers can easily implement vector-like or
	list-like objects as concrete subclasses of Vector or List. In addition,
	a few low-level concrete subclasses of general interest (e.g. DataFrame,
	Rle, and Hits) are implemented in the S4Vectors package itself (many
	more are implemented in the IRanges package and in other Bioconductor
	infrastructure packages)."""

	bioc = "S4Vectors"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/S4Vectors_0.40.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/S4Vectors/S4Vectors_0.40.2.tar.gz"]

	version("0.40.2", md5="ee94f4f6c25dcaf7a50f5814495310e3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.37:", type=("build", "run"))
