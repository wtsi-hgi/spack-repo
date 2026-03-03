# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDmelanogasterUcscDm2Masked(RPackage):
	"""Full masked genome sequences for Drosophila melanogaster (UCSC version dm2)

	Full genome sequences for Drosophila melanogaster (Fly) as provided by UCSC (dm2, Apr. 2004) and stored in Biostrings objects. The sequences are the same as in BSgenome.Dmelanogaster.UCSC.dm2, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Dmelanogaster.UCSC.dm2.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm2.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Dmelanogaster.UCSC.dm2.masked/BSgenome.Dmelanogaster.UCSC.dm2.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="ae7ca3053e97a0d6bd20bc2b9635ecce")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-dmelanogaster-ucsc-dm2", type=("build", "run"))

