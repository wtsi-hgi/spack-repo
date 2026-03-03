# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg38Masked(RPackage):
	"""Full masked genomic sequences for Homo sapiens (UCSC version hg38)

	Full genomic sequences for Homo sapiens as provided by UCSC (genome hg38, based on assembly GRCh38.p14 since 2023/01/31). The sequences are the same as in BSgenome.Hsapiens.UCSC.hg38, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default. The sequences are stored in MaskedDNAString objects.
	"""
	
	bioc = "BSgenome.Hsapiens.UCSC.hg38.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg38.masked_1.4.5.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg38.masked/BSgenome.Hsapiens.UCSC.hg38.masked_1.4.5.tar.gz"]

	version("1.4.5", md5="7570dd1b4f013b3c6acecd68602180b4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.34.9:", type=("build", "run"))
	depends_on("r-bsgenome@1.66.2:", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))

