# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicalignments(RPackage):
	"""Representation and manipulation of short genomic alignments.

	Provides efficient containers for storing and manipulating short genomic
	alignments (typically obtained by aligning short reads to a reference
	genome). This includes read counting, computing the coverage, junction
	detection, and working with the nucleotide content of the alignments."""

	bioc = "GenomicAlignments"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GenomicAlignments_1.38.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GenomicAlignments/GenomicAlignments_1.38.2.tar.gz"]

	version("1.38.2", md5="6b1bbb35176db253124a9e6786104421")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb@1.13.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.9.13:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
