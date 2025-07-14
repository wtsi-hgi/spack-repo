# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtacseqtfea(RPackage):
	"""Transcription Factor Enrichment Analysis for ATAC-seq

	Assay for Transpose-Accessible Chromatin using sequencing (ATAC-seq) is a technique to assess genome-wide chromatin accessibility by probing open chromatin with hyperactive mutant Tn5 Transposase that inserts sequencing adapters into open regions of the genome. ATACseqTFEA is an improvement of the current computational method that detects differential activity of transcription factors (TFs). ATACseqTFEA not only uses the difference of open region information, but also (or emphasizes) the difference of TFs footprints (cutting sites or insertion sites). ATACseqTFEA provides an easy, rigorous way to broadly assess TF activity changes between two conditions.
	"""
	
	homepage = "https://github.com/jianhong/ATACseqTFEA"
	bioc = "ATACseqTFEA"

	version("1.10.0", commit="66f0a543d78536d1ef5e18a84620b8bc77245111")
	version("1.4.0", commit="a8b0929248a7fbe83c6aa5dcc815bf27f5c6b152")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
