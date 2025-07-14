# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCssq(RPackage):
	"""Chip-seq Signal Quantifier Pipeline

	This package is desgined to perform statistical analysis to identify statistically significant differentially bound regions between multiple groups of ChIP-seq dataset.
	"""
	
	bioc = "CSSQ"

	version("1.20.0", commit="1eeb773a6fcdf885d447e4b66dd5cf95f8c2e039")
	version("1.14.0", commit="169f2fd89ff6ba2a95782a1dcd4e7835bd50ad9d")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
