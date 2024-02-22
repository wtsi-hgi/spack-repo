# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocfilecache(RPackage):
	"""Manage Files Across Sessions.

	This package creates a persistent on-disk cache of files that the user
	can add, update, and retrieve. It is useful for managing resources (such
	as custom Txdb objects) that are costly or difficult to create, web
	resources, and data files used across sessions."""

	bioc = "BiocFileCache"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocFileCache_2.10.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocFileCache/BiocFileCache_2.10.1.tar.gz"]

	version("2.10.1", md5="80f9b9c7ef6f3fcb9aaff7125b409137")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dbplyr@1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
