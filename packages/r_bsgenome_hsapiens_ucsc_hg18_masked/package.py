# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg18Masked(RPackage):
	"""Full masked genome sequences for Homo sapiens (UCSC version hg18)

	Full genome sequences for Homo sapiens (Human) as provided by UCSC (hg18, Mar. 2006) and stored in Biostrings objects. The sequences are the same as in BSgenome.Hsapiens.UCSC.hg18, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Hsapiens.UCSC.hg18.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg18.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg18.masked/BSgenome.Hsapiens.UCSC.hg18.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="e6a31e3cba34ce5e0eb6f76d2c19870c")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg18", type=("build", "run"))

