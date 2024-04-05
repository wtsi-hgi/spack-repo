# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg17(RPackage):
	"""Full genome sequences for Homo sapiens (UCSC version hg17)

	Full genome sequences for Homo sapiens (Human) as provided by UCSC (hg17, May 2004) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Hsapiens.UCSC.hg17" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg17_1.3.1000.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg17/BSgenome.Hsapiens.UCSC.hg17_1.3.1000.tar.gz"]

	version("1.3.1000", md5="cbea3029c3d3125a88e6c061c3d3abde", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg17_1.3.1000.tar.gz")
	version("1.3.1000", md5="cbea3029c3d3125a88e6c061c3d3abde", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg17_1.3.1000.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

