# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCneoformansvargrubiikn99NcbiAsm221672v1(RPackage):
	"""Full Genome Sequence for Cryptococcus neoformans var. grubii KN99 (ASM221672v1)

	Full genome sequences for Cryptococcus neoformans var. grubii KN99 (assembly ASM221672v1 assembly accession GCA_002216725.1).
	"""
	
	bioc = "BSgenome.CneoformansVarGrubiiKN99.NCBI.ASM221672v1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.CneoformansVarGrubiiKN99.NCBI.ASM221672v1_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.CneoformansVarGrubiiKN99.NCBI.ASM221672v1/BSgenome.CneoformansVarGrubiiKN99.NCBI.ASM221672v1_1.0.0.tar.gz"]

	version("1.0.0", md5="ea536a15bd932af794f672d9b204c141", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.CneoformansVarGrubiiKN99.NCBI.ASM221672v1_1.0.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

