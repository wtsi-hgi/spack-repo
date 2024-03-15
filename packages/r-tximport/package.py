# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTximport(RPackage):
	"""Import and summarize transcript-level estimates for transcript- and
	gene-level analysis.

	Imports transcript-level abundance, estimated counts and transcript
	lengths, and summarizes into matrices for use with downstream gene-level
	analysis packages. Average transcript length, weighted by sample-
	specific transcript abundance estimates, is provided as a matrix which
	can be used as an offset for different expression of gene-level
	counts."""

	bioc = "tximport"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tximport_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tximport/tximport_1.30.0.tar.gz"]

	version("1.30.0", md5="8bbe549dafbf5b0dfe626f327910a893")

