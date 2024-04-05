# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmusculusUcscMm9Masked(RPackage):
	"""Full masked genome sequences for Mus musculus (UCSC version mm9)

	Full genome sequences for Mus musculus (Mouse) as provided by UCSC (mm9, Jul. 2007) and stored in Biostrings objects. The sequences are the same as in BSgenome.Mmusculus.UCSC.mm9, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Mmusculus.UCSC.mm9.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm9.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmusculus.UCSC.mm9.masked/BSgenome.Mmusculus.UCSC.mm9.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="a5dadab14e55cdfc39649ede7a8483d5")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm9", type=("build", "run"))

