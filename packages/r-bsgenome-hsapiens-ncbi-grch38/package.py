# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensNcbiGrch38(RPackage):
	"""Full genome sequences for Homo sapiens (GRCh38)

	Full genome sequences for Homo sapiens (Human) as provided by NCBI (GRCh38, 2013-12-17) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Hsapiens.NCBI.GRCh38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.NCBI.GRCh38_1.3.1000.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.NCBI.GRCh38/BSgenome.Hsapiens.NCBI.GRCh38_1.3.1000.tar.gz"]

	version("1.3.1000", sha256="812538bdacfd0eb90714916203dec85b22de2a5f7aaf0d0431d0a15370c3e578", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.NCBI.GRCh38_1.3.1000.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

