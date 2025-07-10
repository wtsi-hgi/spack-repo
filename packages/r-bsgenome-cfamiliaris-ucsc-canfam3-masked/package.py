# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCfamiliarisUcscCanfam3Masked(RPackage):
	"""Full masked genome sequences for Canis lupus familiaris (UCSC version canFam3)

	Full genome sequences for Canis lupus familiaris (Dog) as provided by UCSC (canFam3, Sep. 2011) and stored in Biostrings objects. The sequences are the same as in BSgenome.Cfamiliaris.UCSC.canFam3, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Cfamiliaris.UCSC.canFam3.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cfamiliaris.UCSC.canFam3.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Cfamiliaris.UCSC.canFam3.masked/BSgenome.Cfamiliaris.UCSC.canFam3.masked_1.3.99.tar.gz"]

	version("1.3.99", sha256="d4205162077a4fad1959fa6743e3659c057d546b94e7f23c1a7769b2cc43c21f")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-cfamiliaris-ucsc-canfam3", type=("build", "run"))

