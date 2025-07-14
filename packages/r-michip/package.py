# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMichip(RPackage):
	"""MiChip Parsing and Summarizing Functions

	This package takes the MiChip miRNA microarray .grp scanner output files and parses these out, providing summary and plotting functions to analyse MiChip hybridizations. A set of hybridizations is packaged into an ExpressionSet allowing it to be used by other BioConductor packages.
	"""
	
	bioc = "MiChip"

	version("1.62.0", commit="f99b7482b5d6ca83f76e969b997389b70c9b120d")
	version("1.56.0", commit="b3be377398a95dc6e82b5db560a70a1cc206effe")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
