# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDrerioUcscDanrer6Masked(RPackage):
	"""Full masked genome sequences for Danio rerio (UCSC version danRer6)

	Full genome sequences for Danio rerio (Zebrafish) as provided by UCSC (danRer6, Dec. 2008) and stored in Biostrings objects. The sequences are the same as in BSgenome.Drerio.UCSC.danRer6, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Drerio.UCSC.danRer6.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer6.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Drerio.UCSC.danRer6.masked/BSgenome.Drerio.UCSC.danRer6.masked_1.3.99.tar.gz"]

	version("1.3.99", sha256="93e0dd5b73ddcae3cae154a5e9efe545a43886189aeea7ea5b7f96eb7af1af9c")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-drerio-ucsc-danrer6", type=("build", "run"))

