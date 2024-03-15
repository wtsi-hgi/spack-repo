# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXvector(RPackage):
	"""Foundation of external vector representation and manipulation in
	Bioconductor.

	Provides memory efficient S4 classes for storing sequences "externally"
	(e.g. behind an R external pointer, or on disk)."""

	bioc = "XVector"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/XVector_0.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/XVector/XVector_0.42.0.tar.gz"]

	version("0.42.0", md5="f126998c6b563132e51ea31c3995c6b9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
