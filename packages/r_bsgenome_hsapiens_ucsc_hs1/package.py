# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHs1(RPackage):
	"""Full genomic sequences for UCSC genome hs1 (Homo sapiens)

	Full genomic sequences for UCSC genome hs1 (the hs1 genome is based on assembly T2T-CHM13v2.0, with GenBank assembly accession GCA_009914755.4). The sequences are stored in DNAString objects.
	"""
	
	bioc = "BSgenome.Hsapiens.UCSC.hs1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hs1_1.4.4.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hs1/BSgenome.Hsapiens.UCSC.hs1_1.4.4.tar.gz"]

	version("1.4.4", md5="5812c5670f51a5c58a9da9e042e7e440", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hs1_1.4.4.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

