# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiens1000genomesHs37d5(RPackage):
	"""1000genomes Reference Genome Sequence (hs37d5)

	1000genomes Phase2 Reference Genome Sequence (hs37d5), based on NCBI GRCh37.
	"""
	
	bioc = "BSgenome.Hsapiens.1000genomes.hs37d5" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.1000genomes.hs37d5_0.99.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.1000genomes.hs37d5/BSgenome.Hsapiens.1000genomes.hs37d5_0.99.1.tar.gz"]

	version("0.99.1", md5="164e1692d38fefa499c2c8ac5fc22793", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.1000genomes.hs37d5_0.99.1.tar.gz")

	depends_on("r-bsgenome@1.34:", type=("build", "run"))

