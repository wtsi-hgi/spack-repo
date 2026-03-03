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

	version("1.4.1", md5="60d3fb201e0b1475912aaf681927096d", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn6_1.4.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

