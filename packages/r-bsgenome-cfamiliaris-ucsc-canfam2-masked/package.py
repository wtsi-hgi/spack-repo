# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCfamiliarisUcscCanfam2Masked(RPackage):
	"""Full masked genome sequences for Canis lupus familiaris (UCSC version canFam2)

	Full genome sequences for Canis lupus familiaris (Dog) as provided by UCSC (canFam2, May 2005) and stored in Biostrings objects. The sequences are the same as in BSgenome.Cfamiliaris.UCSC.canFam2, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Cfamiliaris.UCSC.canFam2.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cfamiliaris.UCSC.canFam2.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Cfamiliaris.UCSC.canFam2.masked/BSgenome.Cfamiliaris.UCSC.canFam2.masked_1.3.99.tar.gz"]

	version("1.3.99", sha256="1f5738522fb7aef718154221cd5060ea92a04b56387670404b259d3f8e442090")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-cfamiliaris-ucsc-canfam2", type=("build", "run"))

