# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminaio(RPackage):
	"""Parsing Illumina Microarray Output Files.

	Tools for parsing Illumina's microarray output files, including IDAT."""

	bioc = "illuminaio"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/illuminaio_0.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/illuminaio/illuminaio_0.44.0.tar.gz"]

	version("0.44.0", md5="5bf0b60249c92ef8408564391a69a97d")

	depends_on("r-base64", type=("build", "run"))
