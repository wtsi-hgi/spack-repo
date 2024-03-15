# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDmelanogasterUcscDm6(RPackage):
	"""Full genome sequences for Drosophila melanogaster (UCSC version dm6)

	Full genome sequences for Drosophila melanogaster (Fly) as provided by UCSC (dm6, Aug. 2014) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Dmelanogaster.UCSC.dm6" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm6_1.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Dmelanogaster.UCSC.dm6/BSgenome.Dmelanogaster.UCSC.dm6_1.4.1.tar.gz"]

	version("1.4.1", md5="f9d6e406b7893a17c08edd4521c2802f", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm6_1.4.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation