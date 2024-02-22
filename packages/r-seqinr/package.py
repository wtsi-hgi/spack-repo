# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqinr(RPackage):
	"""Biological Sequences Retrieval and Analysis.

	Exploratory data analysis and data visualization for biological sequence
	(DNA and protein) data. Seqinr includes utilities for sequence data
	management under the ACNUC system described in Gouy, M. et al. (1984)
	Nucleic Acids Res. 12:121-127 <doi:10.1093/nar/12.1Part1.121>."""

	cran = "seqinr"

	version("4.2-36", md5="f8b8a5c41363cddfa1f6073890d99967")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
