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

	version("1.4.0", sha256="4b58a9e8510da0f5a0f9f00c2bdadc5ca6c2e4e061c3a3822b3d535adb1fbdea", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Scerevisiae.UCSC.sacCer1_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

