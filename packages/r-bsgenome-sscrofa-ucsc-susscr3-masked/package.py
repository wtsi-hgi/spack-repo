# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeSscrofaUcscSusscr3Masked(RPackage):
	"""Full masked genome sequences for Sus scrofa (UCSC version susScr3)

	Full genome sequences for Sus scrofa (Pig) as provided by UCSC (susScr3, Aug. 2011) and stored in Biostrings objects. The sequences are the same as in BSgenome.Sscrofa.UCSC.susScr3, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Sscrofa.UCSC.susScr3.masked" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Sscrofa.UCSC.susScr3.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Sscrofa.UCSC.susScr3.masked/BSgenome.Sscrofa.UCSC.susScr3.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="fd240651d22d169fd1e27a2b66e40dd7")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-sscrofa-ucsc-susscr3", type=("build", "run"))

	# annotation