# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeRnorvegicusUcscRn5Masked(RPackage):
	"""Full masked genome sequences for Rattus norvegicus (UCSC version rn5)

	Full genome sequences for Rattus norvegicus (Rat) as provided by UCSC (rn5, Mar. 2012) and stored in Biostrings objects. The sequences are the same as in BSgenome.Rnorvegicus.UCSC.rn5, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Rnorvegicus.UCSC.rn5.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn5.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Rnorvegicus.UCSC.rn5.masked/BSgenome.Rnorvegicus.UCSC.rn5.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="663233774b79012cb2cc08224ac275ed")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-rnorvegicus-ucsc-rn5", type=("build", "run"))

