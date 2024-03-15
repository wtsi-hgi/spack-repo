# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmusculusUcscMm10(RPackage):
	"""Full genome sequences for Mus musculus (UCSC version mm10, based on GRCm38.p6)

	Full genome sequences for Mus musculus (Mouse) as provided by UCSC (mm10, based on GRCm38.p6) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mmusculus.UCSC.mm10" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm10_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmusculus.UCSC.mm10/BSgenome.Mmusculus.UCSC.mm10_1.4.3.tar.gz"]

	version("1.4.3", md5="ffddc2e035527ed1a1e201ac4cc0b1f3", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm10_1.4.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

	# annotation