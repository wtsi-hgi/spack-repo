# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg18(RPackage):
	"""Full genome sequences for Homo sapiens (UCSC version hg18)

	Full genome sequences for Homo sapiens (Human) as provided by UCSC (hg18, Mar. 2006) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Hsapiens.UCSC.hg18" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg18_1.3.1000.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg18/BSgenome.Hsapiens.UCSC.hg18_1.3.1000.tar.gz"]

	version("1.3.1000", md5="51bb2e1ed4009860bb21aaac32fffd9c", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg18_1.3.1000.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation