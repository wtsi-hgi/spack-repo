# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocversion(RPackage):
	"""Set the appropriate version of Bioconductor packages.

	This package provides repository information for the appropriate
	version of Bioconductor."""

	bioc = "BiocVersion"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocVersion_3.18.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocVersion/BiocVersion_3.18.1.tar.gz"]

	version("3.18.1", md5="46dbe2f6ca9c058b24da1bd98f79631e")

	depends_on("r@4.3:", type=("build", "run"))
