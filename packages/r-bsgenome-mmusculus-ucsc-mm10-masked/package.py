# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmusculusUcscMm10Masked(RPackage):
	"""Full masked genome sequences for Mus musculus (UCSC genome mm10, based on GRCm38.p6)

	Full genome sequences for Mus musculus (Mouse) as provided by UCSC (genome mm10, based on GRCm38.p6) and stored in Biostrings objects. The sequences are the same as in BSgenome.Mmusculus.UCSC.mm10, except that each of them has the 2 following masks on top: (1) the mask of assembly gaps (AGAPS mask), and (2) the mask of intra-contig ambiguities (AMB mask).
	"""
	
	bioc = "BSgenome.Mmusculus.UCSC.mm10.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm10.masked_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmusculus.UCSC.mm10.masked/BSgenome.Mmusculus.UCSC.mm10.masked_1.4.3.tar.gz"]

	version("1.4.3", sha256="ec89d19b63e34e32c8dd7dc4894ad544f0aec0a7deb3b554a9b74a6244166510")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm10", type=("build", "run"))

