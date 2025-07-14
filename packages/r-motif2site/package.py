# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotif2site(RPackage):
	"""Detect binding sites from motifs and ChIP-seq experiments, and compare binding sites across conditions

	Detect binding sites using motifs IUPAC sequence or bed coordinates and ChIP-seq experiments in bed or bam format. Combine/compare binding sites across experiments, tissues, or conditions. All normalization and differential steps are done using TMM-GLM method. Signal decomposition is done by setting motifs as the centers of the mixture of normal distribution curves.
	"""
	
	bioc = "Motif2Site"

	version("1.12.0", commit="c927d2810af7a60ba727fb54ef87185999ebb7d0")
	version("1.6.0", commit="9150ae703cbb8fb07b7e856daf84adb110878ab8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
