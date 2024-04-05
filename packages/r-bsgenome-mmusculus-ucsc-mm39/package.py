# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmusculusUcscMm39(RPackage):
	"""Full genome sequences for Mus musculus (UCSC genome mm39, based on GRCm39)

	Full genome sequences for Mus musculus (Mouse) as provided by UCSC (genome mm39, based on assembly GRCm39) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mmusculus.UCSC.mm39" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm39_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmusculus.UCSC.mm39/BSgenome.Mmusculus.UCSC.mm39_1.4.3.tar.gz"]

	version("1.4.3", md5="a130ef50dd55da9fd341e6c90b22637b", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm39_1.4.3.tar.gz")
	version("1.4.3", md5="a130ef50dd55da9fd341e6c90b22637b", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm39_1.4.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

