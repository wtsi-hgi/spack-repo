# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeBtaurusUcscBostau9Masked(RPackage):
	"""Full masked genome sequences for Bos taurus (UCSC version bosTau9)

	Full genome sequences for Bos taurus (Cow) as provided by UCSC (genome bosTau9) and stored in Biostrings objects. The sequences are the same as in BSgenome.Btaurus.UCSC.bosTau9, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Btaurus.UCSC.bosTau9.masked" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau9.masked_1.4.4.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Btaurus.UCSC.bosTau9.masked/BSgenome.Btaurus.UCSC.bosTau9.masked_1.4.4.tar.gz"]

	version("1.4.4", md5="c96bd95c3b791d712aa5cb8c96f9c937")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-btaurus-ucsc-bostau9", type=("build", "run"))

	# annotation