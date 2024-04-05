# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeGaculeatusUcscGasacu1(RPackage):
	"""Full genome sequences for Gasterosteus aculeatus (UCSC version gasAcu1)

	Full genome sequences for Gasterosteus aculeatus (Stickleback) as provided by UCSC (gasAcu1, Feb. 2006) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Gaculeatus.UCSC.gasAcu1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Gaculeatus.UCSC.gasAcu1_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Gaculeatus.UCSC.gasAcu1/BSgenome.Gaculeatus.UCSC.gasAcu1_1.4.0.tar.gz"]

	version("1.4.0", md5="412aa0570d9c556861b7bb9a5bbc2007", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Gaculeatus.UCSC.gasAcu1_1.4.0.tar.gz")
	version("1.4.0", md5="412aa0570d9c556861b7bb9a5bbc2007", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Gaculeatus.UCSC.gasAcu1_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

