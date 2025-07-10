# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeRnorvegicusUcscRn6(RPackage):
	"""Full genome sequences for Rattus norvegicus (UCSC version rn6)

	Full genome sequences for Rattus norvegicus (Rat) as provided by UCSC (rn6, Jul. 2014) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Rnorvegicus.UCSC.rn6" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn6_1.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Rnorvegicus.UCSC.rn6/BSgenome.Rnorvegicus.UCSC.rn6_1.4.1.tar.gz"]

	version("1.4.1", sha256="b5d6b1d078e58eb615258b67b6c0020d127464a6e0cf62a1ac3afb5de871dbd3", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn6_1.4.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

