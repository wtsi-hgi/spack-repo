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

	version("1.3.99", sha256="6a556f64c9da0a0895dbe7659318522cf0902d8c07f887a75111ddb9c5c5e915")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-tguttata-ucsc-taegut1", type=("build", "run"))

