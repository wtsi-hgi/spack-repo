# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDmelanogasterUcscDm2(RPackage):
	"""Full genome sequences for Drosophila melanogaster (UCSC version dm2)

	Full genome sequences for Drosophila melanogaster (Fly) as provided by UCSC (dm2, Apr. 2004) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Dmelanogaster.UCSC.dm2" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm2_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Dmelanogaster.UCSC.dm2/BSgenome.Dmelanogaster.UCSC.dm2_1.4.0.tar.gz"]

	version("1.4.0", md5="ebc88df5595fc7aad588b8f3f7de4784", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm2_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation