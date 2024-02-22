# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtgenerics(RPackage):
	"""S4 generic functions for Bioconductor proteomics infrastructure.

	S4 generic functions needed by Bioconductor proteomics packages."""

	bioc = "ProtGenerics"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ProtGenerics_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ProtGenerics/ProtGenerics_1.34.0.tar.gz"]

	version("1.34.0", md5="5d55c00588169aa089bb457e2d94669a")

