# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecipher(RPackage):
	"""Tools for curating, analyzing, and manipulating biological sequences.

	A toolset for deciphering and managing biological sequences."""

	bioc = "DECIPHER"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DECIPHER_2.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DECIPHER/DECIPHER_2.30.0.tar.gz"]

	version("2.30.0", md5="0a32c782d61a604dc3594c684daa8c75")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsqlite@1.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
