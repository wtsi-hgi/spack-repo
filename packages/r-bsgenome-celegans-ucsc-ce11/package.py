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
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce11_1.4.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Celegans.UCSC.ce11/BSgenome.Celegans.UCSC.ce11_1.4.2.tar.gz"]

	version("1.4.2", md5="b80e24149a0c6ed323d0c9a6d112ef52", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce11_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation