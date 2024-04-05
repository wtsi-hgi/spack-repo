# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDrerioUcscDanrer6(RPackage):
	"""Full genome sequences for Danio rerio (UCSC version danRer6)

	Full genome sequences for Danio rerio (Zebrafish) as provided by UCSC (danRer6, Dec. 2008) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Drerio.UCSC.danRer6" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer6_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Drerio.UCSC.danRer6/BSgenome.Drerio.UCSC.danRer6_1.4.0.tar.gz"]

	version("1.4.0", md5="537d37d29d97ae0c31d77decc67b25b0", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer6_1.4.0.tar.gz")
	version("1.4.0", md5="537d37d29d97ae0c31d77decc67b25b0", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer6_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

