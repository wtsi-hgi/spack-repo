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

	version("1.4.1", md5="c33e71746ce551bcbcd22be1979aee63", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mfuro.UCSC.musFur1_1.4.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation