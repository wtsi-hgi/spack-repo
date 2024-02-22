# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakecdfenv(RPackage):
	"""CDF Environment Maker.

	This package has two functions. One reads a Affymetrix chip description
	file (CDF) and creates a hash table environment containing the
	location/probe set membership mapping. The other creates a package that
	automatically loads that environment."""

	bioc = "makecdfenv"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/makecdfenv_1.78.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/makecdfenv/makecdfenv_1.78.0.tar.gz"]

	version("1.78.0", md5="b5c8877fd5b09fbb4d3656490fa7eb64")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-affyio", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
