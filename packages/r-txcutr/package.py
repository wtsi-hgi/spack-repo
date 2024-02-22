# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxcutr(RPackage):
	"""Transcriptome CUTteR

	Various mRNA sequencing library preparation methods generate sequencing reads specifically from the transcript ends. Analyses that focus on quantification of isoform usage from such data can be aided by using truncated versions of transcriptome annotations, both at the alignment or pseudo-alignment stage, as well as in downstream analysis. This package implements some convenience methods for readily generating such truncated annotations and their corresponding sequences.
	"""
	
	bioc = "txcutr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/txcutr_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/txcutr/txcutr_1.8.0.tar.gz"]

	version("1.8.0", md5="10d81d02156a45cebc08845455180010")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
