# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqlogo(RPackage):
	"""Sequence logos for DNA sequence alignments.

	seqLogo takes the position weight matrix of a DNA sequence motif and
	plots the corresponding sequence logo as introduced by Schneider and
	Stephens (1990)."""

	bioc = "seqLogo"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/seqLogo_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/seqLogo/seqLogo_1.68.0.tar.gz"]

	version("1.68.0", md5="0771c35a7929a3e71aa5eebaf4a624ef")

	depends_on("r@4.2:", type=("build", "run"))
