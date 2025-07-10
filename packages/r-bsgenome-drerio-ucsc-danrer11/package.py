# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDrerioUcscDanrer11(RPackage):
	"""Full genome sequences for Danio rerio (UCSC version danRer11)

	Full genome sequences for Danio rerio (Zebrafish) as provided by UCSC (danRer11, May 2017) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Drerio.UCSC.danRer11" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer11_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Drerio.UCSC.danRer11/BSgenome.Drerio.UCSC.danRer11_1.4.2.tar.gz"]

	version("1.4.2", sha256="9b4cce02a910493448e4cf3669a84a3fad10adc99e68269fed52ec8f2b124921", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer11_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

