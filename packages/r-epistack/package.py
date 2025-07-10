# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpistack(RPackage):
	"""Heatmaps of Stack Profiles from Epigenetic Signals

	The epistack package main objective is the visualizations of stacks of genomic tracks (such as, but not restricted to, ChIP-seq, ATAC-seq, DNA methyation or genomic conservation data) centered at genomic regions of interest. epistack needs three different inputs: 1) a genomic score objects, such as ChIP-seq coverage or DNA methylation values, provided as a `GRanges` (easily obtained from `bigwig` or `bam` files). 2) a list of feature of interest, such as peaks or transcription start sites, provided as a `GRanges` (easily obtained from `gtf` or `bed` files). 3) a score to sort the features, such as peak height or gene expression value.
	"""
	
	homepage = "https://github.com/GenEpi-GenPhySE/epistack"
	bioc = "epistack" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/epistack_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/epistack/epistack_1.8.0.tar.gz"]

	version("1.8.0", sha256="738b2cf0a8c23ad732af1703448778c4ff5bfe671facc9cd22dffd8a7b0bf254")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
