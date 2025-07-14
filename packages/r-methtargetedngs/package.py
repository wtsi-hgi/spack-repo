# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethtargetedngs(RPackage):
	"""Perform Methylation Analysis on Next Generation Sequencing Data

	Perform step by step methylation analysis of Next Generation Sequencing data.
	"""
	
	bioc = "MethTargetedNGS"

	version("1.40.0", commit="6c164a1ae868ca3eed9a88986ed1aea7005dd27e")
	version("1.34.0", commit="b3b59e3c671ef7a9ee132818598f82d59d71b7c4")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("hmmer@3:", type=("build", "link", "run"))
