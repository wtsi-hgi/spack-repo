# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTin(RPackage):
	"""Transcriptome instability analysis

	The TIN package implements a set of tools for transcriptome instability analysis based on exon expression profiles. Deviating exon usage is studied in the context of splicing factors to analyse to what degree transcriptome instability is correlated to splicing factor expression. In the transcriptome instability correlation analysis, the data is compared to both random permutations of alternative splicing scores and expression of random gene sets.
	"""
	
	bioc = "TIN" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TIN_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TIN/TIN_1.34.0.tar.gz"]

	version("1.34.0", md5="33dbf5f6f5fada307f20f5a9b8d6f8a8")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-aroma-affymetrix", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-squash", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
