# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeTguttataUcscTaegut1Masked(RPackage):
	"""Full masked genome sequences for Taeniopygia guttata (UCSC version taeGut1)

	Full genome sequences for Taeniopygia guttata (Zebra finch) as provided by UCSC (taeGut1, Jul. 2008) and stored in Biostrings objects. The sequences are the same as in BSgenome.Tguttata.UCSC.taeGut1, except that each of them has the 2 following masks on top: (1) the mask of assembly gaps (AGAPS mask), and (2) the mask of intra-contig ambiguities (AMB mask). Both masks are "active" by default.
	"""
	
	bioc = "BSgenome.Tguttata.UCSC.taeGut1.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Tguttata.UCSC.taeGut1.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Tguttata.UCSC.taeGut1.masked/BSgenome.Tguttata.UCSC.taeGut1.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="63684abb5b330bb54ff89fe78f2e6444")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-tguttata-ucsc-taegut1", type=("build", "run"))

	# annotation