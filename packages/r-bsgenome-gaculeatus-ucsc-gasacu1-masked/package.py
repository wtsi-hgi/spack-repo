# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeGaculeatusUcscGasacu1Masked(RPackage):
	"""Full masked genome sequences for Gasterosteus aculeatus (UCSC version gasAcu1)

	Full genome sequences for Gasterosteus aculeatus (Stickleback) as provided by UCSC (gasAcu1, Feb. 2006) and stored in Biostrings objects. The sequences are the same as in BSgenome.Gaculeatus.UCSC.gasAcu1, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Gaculeatus.UCSC.gasAcu1.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Gaculeatus.UCSC.gasAcu1.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Gaculeatus.UCSC.gasAcu1.masked/BSgenome.Gaculeatus.UCSC.gasAcu1.masked_1.3.99.tar.gz"]

	version("1.3.99", sha256="7d47459528664ecb7326bcaed0b36ee5f1f7e18ac4d30f14609962b40debe28d")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-gaculeatus-ucsc-gasacu1", type=("build", "run"))

