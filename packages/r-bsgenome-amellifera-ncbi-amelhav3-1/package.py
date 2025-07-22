# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAmelliferaNcbiAmelhav31(RPackage):
	"""Full genome sequences for Apis mellifera (Amel_HAv3.1)

	Full genome sequences for Apis mellifera as provided by NCBI (assembly Amel_HAv3.1, assembly accession GCF_003254395.2) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Amellifera.NCBI.AmelHAv3.1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Amellifera.NCBI.AmelHAv3.1_1.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Amellifera.NCBI.AmelHAv3.1/BSgenome.Amellifera.NCBI.AmelHAv3.1_1.5.0.tar.gz"]

	version("1.5.0", sha256="8768247e7b846ad16d3265633a5837b0086d7a7ea1f4465c8525639a09adf4b1", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Amellifera.NCBI.AmelHAv3.1_1.5.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

