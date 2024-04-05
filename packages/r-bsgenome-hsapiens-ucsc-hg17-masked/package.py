# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg17Masked(RPackage):
	"""Full masked genome sequences for Homo sapiens (UCSC version hg17)

	Full genome sequences for Homo sapiens (Human) as provided by UCSC (hg17, May 2004) and stored in Biostrings objects. The sequences are the same as in BSgenome.Hsapiens.UCSC.hg17, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Hsapiens.UCSC.hg17.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg17.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg17.masked/BSgenome.Hsapiens.UCSC.hg17.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="ff6ee5196f234c5a2a3bcdd052c3c08e")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg17", type=("build", "run"))

