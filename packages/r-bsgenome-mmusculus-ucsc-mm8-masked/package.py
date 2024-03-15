# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmusculusUcscMm8Masked(RPackage):
	"""Full masked genome sequences for Mus musculus (UCSC version mm8)

	Full genome sequences for Mus musculus (Mouse) as provided by UCSC (mm8, Feb. 2006) and stored in Biostrings objects. The sequences are the same as in BSgenome.Mmusculus.UCSC.mm8, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Mmusculus.UCSC.mm8.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm8.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmusculus.UCSC.mm8.masked/BSgenome.Mmusculus.UCSC.mm8.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="5809f925e0fe7c4b73b78a90c9a36fdd")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm8", type=("build", "run"))

	# annotation