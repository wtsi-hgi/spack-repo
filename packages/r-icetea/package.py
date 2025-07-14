# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcetea(RPackage):
	"""Integrating Cap Enrichment with Transcript Expression Analysis

	icetea (Integrating Cap Enrichment with Transcript Expression Analysis) provides functions for end-to-end analysis of multiple 5'-profiling methods such as CAGE, RAMPAGE and MAPCap, beginning from raw reads to detection of transcription start sites using replicates. It also allows performing differential TSS detection between group of samples, therefore, integrating the mRNA cap enrichment information with transcript expression analysis.
	"""
	
	homepage = "https://github.com/vivekbhr/icetea"
	bioc = "icetea"

	version("1.26.0", commit="a72364fea44dba639ff4a25d8310af6438a282e6")
	version("1.20.0", commit="7b58dbe6276ede01301e9810dde89ad8aad51344")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-csaw", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-txdb-dmelanogaster-ucsc-dm6-ensgene", type=("build", "run"))
