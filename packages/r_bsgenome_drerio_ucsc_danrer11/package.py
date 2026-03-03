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

	version("1.4.2", md5="cd586da56ca88ccebb85804f992ba204", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer11_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

