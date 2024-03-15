# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicranges(RPackage):
	"""Representation and manipulation of genomic intervals.

	The ability to efficiently represent and manipulate genomic annotations
	and alignments is playing a central role when it comes to analyzing
	high-throughput sequencing data (a.k.a. NGS data). The GenomicRanges
	package defines general purpose containers for storing and manipulating
	genomic intervals and variables defined along a genome. More specialized
	containers for representing and manipulating short alignments against a
	reference genome, or a matrix-like summarization of an experiment, are
	defined in the GenomicAlignments and SummarizedExperiment packages,
	respectively. Both packages build on top of the GenomicRanges
	infrastructure."""

	bioc = "GenomicRanges"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GenomicRanges_1.54.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GenomicRanges/GenomicRanges_1.54.1.tar.gz"]

	version("1.54.1", md5="19fe37133cae70c1c3a1a164e6c8eaed")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.37:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
	depends_on("r-xvector@0.29.2:", type=("build", "run"))
