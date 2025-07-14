# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicdistributions(RPackage):
	"""GenomicDistributions: fast analysis of genomic intervals with Bioconductor

	If you have a set of genomic ranges, this package can help you with visualization and comparison. It produces several kinds of plots, for example: Chromosome distribution plots, which visualize how your regions are distributed over chromosomes; feature distance distribution plots, which visualizes how your regions are distributed relative to a feature of interest, like Transcription Start Sites (TSSs); genomic partition plots, which visualize how your regions overlap given genomic features such as promoters, introns, exons, or intergenic regions. It also makes it easy to compare one set of ranges to another.
	"""
	
	homepage = "http://code.databio.org/GenomicDistributions"
	bioc = "GenomicDistributions"

	version("1.16.1", commit="2f86fb9f41323f2a5a15f2530ef68f6c6d8d0626")
	version("1.10.0", commit="1b03a0239da68172e00f97ea7c33d6fb00d33b1f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
