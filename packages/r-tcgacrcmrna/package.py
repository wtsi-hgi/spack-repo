# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgacrcmrna(RPackage):
	"""TCGA CRC 450 mRNA dataset

	colorectal cancer mRNA profile provided by TCGA
	"""
	
	bioc = "TCGAcrcmRNA" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TCGAcrcmRNA_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TCGAcrcmRNA/TCGAcrcmRNA_1.22.0.tar.gz"]

	version("1.22.0", md5="bb9300e6ad6e4e5435a31487fdc22ed6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

