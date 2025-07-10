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

	version("1.4.0", sha256="5196a651195d1d1faba65fdbcb4823f7acbdcfc0260ff25c127e8bd82e834c40", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer6_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

