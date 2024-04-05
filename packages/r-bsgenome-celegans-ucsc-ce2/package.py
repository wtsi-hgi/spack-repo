# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCelegansUcscCe2(RPackage):
	"""Full genome sequences for Caenorhabditis elegans (UCSC version ce2)

	Full genome sequences for Caenorhabditis elegans (Worm) as provided by UCSC (ce2, Mar. 2004) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Celegans.UCSC.ce2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce2_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Celegans.UCSC.ce2/BSgenome.Celegans.UCSC.ce2_1.4.0.tar.gz"]

	version("1.4.0", md5="b2bf7eec2b07685cf9dcdf42840db208", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce2_1.4.0.tar.gz")
	version("1.4.0", md5="b2bf7eec2b07685cf9dcdf42840db208", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce2_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

