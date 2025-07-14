# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeat(RPackage):
	"""BEAT - BS-Seq Epimutation Analysis Toolkit

	Model-based analysis of single-cell methylation data
	"""
	
	bioc = "BEAT"

	version("1.46.0", commit="e78cc42dd8b7a592f091917ab33ea077a9447c8d")
	version("1.40.0", commit="27254d06458ea8048189b232a40ef2070c3e62ec")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
