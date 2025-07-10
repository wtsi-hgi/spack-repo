# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMfuroUcscMusfur1(RPackage):
	"""Full genome sequences for Mustela putorius furo (UCSC version musFur1)

	Full genome sequences for Mustela putorius furo (Ferret) as provided by UCSC (musFur1, Apr. 2011) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mfuro.UCSC.musFur1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mfuro.UCSC.musFur1_1.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mfuro.UCSC.musFur1/BSgenome.Mfuro.UCSC.musFur1_1.4.1.tar.gz"]

	version("1.4.1", sha256="32bd14393defc207834688b5711be35658509d854e1df73798da8c1954320530", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mfuro.UCSC.musFur1_1.4.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

