# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfeaChip(RPackage):
	"""Analyze Transcription Factor Enrichment

	Package to analize transcription factor enrichment in a gene set using data from ChIP-Seq experiments.
	"""
	
	bioc = "TFEA.ChIP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TFEA.ChIP_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TFEA.ChIP/TFEA.ChIP_1.22.0.tar.gz"]

	version("1.22.0", md5="86f7ae5bb16ceaf9fbdc01d0cc606c42")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
