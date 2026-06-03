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
	git = "https://git.bioconductor.org/packages/GenomicDistributions.git"

	version("1.12.0", tag="RELEASE_3_19")
	version("1.10.0", tag="RELEASE_3_18")

	with default_args(type=("build", "run")):
		depends_on("r@4:")
		depends_on("r-iranges")
		depends_on("r-genomicranges")
		depends_on("r-data-table")
		depends_on("r-ggplot2")
		depends_on("r-reshape2")
		depends_on("r-biostrings@2.70.3:", when="@1.12:")
		depends_on("r-biostrings")
		depends_on("r-plyr")
		depends_on("r-dplyr")
		depends_on("r-scales")
		depends_on("r-broom")
		depends_on("r-genomeinfodb")