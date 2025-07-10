# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCelegansUcscCe11(RPackage):
	"""Full genome sequences for Caenorhabditis elegans (UCSC version ce11)

	Full genome sequences for Caenorhabditis elegans (Worm) as provided by UCSC (ce11, Feb. 2013) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Celegans.UCSC.ce11" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce11_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Celegans.UCSC.ce11/BSgenome.Celegans.UCSC.ce11_1.4.2.tar.gz"]

	version("1.4.2", sha256="bc4c0f2afd3e736444482a0fe9e04023bd00c27fad4663810b3be24b9feb8b34", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce11_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

