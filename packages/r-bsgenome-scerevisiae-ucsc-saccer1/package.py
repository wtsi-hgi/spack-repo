# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeScerevisiaeUcscSaccer1(RPackage):
	"""Saccharomyces cerevisiae (Yeast) full genome (UCSC version sacCer1)

	Saccharomyces cerevisiae (Yeast) full genome as provided by UCSC (sacCer1, Oct. 2003) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Scerevisiae.UCSC.sacCer1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Scerevisiae.UCSC.sacCer1_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Scerevisiae.UCSC.sacCer1/BSgenome.Scerevisiae.UCSC.sacCer1_1.4.0.tar.gz"]

	version("1.4.0", md5="ad4c29c16a9635088bf13872b4a02ed4", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Scerevisiae.UCSC.sacCer1_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

