# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCelegansUcscCe10(RPackage):
	"""Full genome sequences for Caenorhabditis elegans (UCSC version ce10)

	Full genome sequences for Caenorhabditis elegans (Worm) as provided by UCSC (ce10, Oct. 2010) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Celegans.UCSC.ce10" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce10_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Celegans.UCSC.ce10/BSgenome.Celegans.UCSC.ce10_1.4.0.tar.gz"]

	version("1.4.0", md5="98a8ca836d6db23e46674552669d7942", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce10_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

