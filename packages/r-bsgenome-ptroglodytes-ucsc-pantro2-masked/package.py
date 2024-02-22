# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePtroglodytesUcscPantro2Masked(RPackage):
	"""Full masked genome sequences for Pan troglodytes (UCSC version panTro2)

	Full genome sequences for Pan troglodytes (Chimp) as provided by UCSC (panTro2, Mar. 2006) and stored in Biostrings objects. The sequences are the same as in BSgenome.Ptroglodytes.UCSC.panTro2, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Ptroglodytes.UCSC.panTro2.masked" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro2.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Ptroglodytes.UCSC.panTro2.masked/BSgenome.Ptroglodytes.UCSC.panTro2.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="e6d069be23712b483b4e4c71554594cf")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-ptroglodytes-ucsc-pantro2", type=("build", "run"))

	# annotation