# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrcl18(RPackage):
	"""CRC cell line dataset

	colorectal cancer mRNA and miRNA on 18 cell lines
	"""
	
	bioc = "CRCL18"

	version("1.28.0", commit="e7ad40831c757c02dc0474a6550efe62ba0776d6")
	version("1.22.0", commit="d4dcac2e4fd03e691c0e333691c0b27c55e0173e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

